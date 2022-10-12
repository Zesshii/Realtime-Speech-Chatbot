import speech_to_text as stt
import text_to_speech as tts
import get_input_output_devices as iod
import chatbot as cb
import pre_config_inputs as pci

OUTPUT_FILE = "speech.json"  # must be json file

stt = stt.SpeechToText()
iod = iod.Devices()

# pre-config input
pci.is_text_based()
pci.see_device_list()
device_index = pci.enter_device_index()
loopback = pci.is_speaker_output()

# run program
running = True
while running:
    audio = stt.get_audio(is_loopback=loopback, device=device_index)
    text = stt.speech_to_text(audio_data=audio)
    stt.text_to_file(text=text, file=OUTPUT_FILE)
    message = stt.read_text(file=OUTPUT_FILE)  # this displays the last line added to the json file
    response = cb.chatbot_response(message=message)  # gets a response from chatbot
    speech = tts.say(text=response)  # response is converted into audible speech
