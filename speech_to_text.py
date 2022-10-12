import speech_recognition as sr
import pyaudiowpatch as pyaudio
from datetime import datetime as dt
import json

# initialize the recognizer
r = sr.Recognizer()

# initialize datetime and format
now = dt.now()
time = now.strftime("%d/%m/%y %H:%M:%S")


class SpeechToText:
    def __init__(self):
        print("Initializing speech to text...")

    def get_audio(self, is_loopback, device):
        if is_loopback:
            """
            code snippet from s0d3s' PyAudioWPatch loopback example
            link: https://github.com/s0d3s/PyAudioWPatch
            """
            print("\nUsing loopback...")
            with pyaudio.PyAudio() as p:
                try:
                    # get default wasapi info
                    wasapi_info = p.get_host_api_info_by_type(pyaudio.paWASAPI)
                except OSError:
                    print("WASAPI not detected in system...")

                # get default wasapi speakers
                default_speakers = p.get_device_info_by_index(wasapi_info["defaultOutputDevice"])

                if not default_speakers["isLoopbackDevice"]:
                    for loopback in p.get_loopback_device_info_generator():
                        """
                        Try to find loopback device with same name(and [Loopback suffix]).
                        Unfortunately, this is the most adequate way at the moment.
                        """
                        if default_speakers["name"] in loopback["name"]:
                            default_speakers = loopback
                            break
                    else:
                        print(
                            "Default loopback output device not found."
                            "\nRun this to check available devices."
                            "\nExiting..."
                            "\n")
                        exit()

                print(f"Recording from: ({default_speakers['index']}){default_speakers['name']}")
                with sr.Microphone(device_index=device) as source:
                    # read the audio data from default speakers
                    r.adjust_for_ambient_noise(source)  # listen for 1 second to adjust
                    print("\nListening...")
                    audio_data = r.listen(source)
                    return audio_data
        else:
            with sr.Microphone() as source:
                # read the audio data from default microphone
                r.adjust_for_ambient_noise(source)  # listen for 1 second to adjust
                print("\nListening...")
                audio_data = r.listen(source)
                return audio_data

    def speech_to_text(self, audio_data):
        try:
            print("Converting...")
            text = r.recognize_google(audio_data=audio_data)
            return text
        except sr.UnknownValueError:
            print("Could not parse audio...")
            return 0

    def text_to_file(self, text, file):
        if text == 0:
            print("There's nothing to write...")
            return 0
        try:
            # get the old data
            with open(file, mode='r', encoding='utf-8') as data:
                file_data = json.load(data)

            # append the new data
            with open(file, mode='w', encoding='utf-8') as new_data:
                new_text = {
                    'datetime': time,
                    'text': text
                }
                file_data.append(new_text)
                json.dump(file_data, new_data)

        except FileNotFoundError:
            print("File not found...")

    def read_text(self, file):
        try:
            with open(file, mode='r', encoding='utf-8') as data:
                new_data = json.load(data)
                message = new_data[-1]['text']
                print("Heard this:", message)
                return message
        except FileNotFoundError:
            print("File not found...")
            
