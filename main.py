import speech_to_text as stt
import text_to_speech as tts
import get_input_output_devices as iod
import chatbot as cb
import pre_config_inputs as pci
import queries as qy

OUTPUT_FILE = "speech.json"
# OUTPUT_FILE = "Realtime-Speech-Chatbot/speech.json"

stt = stt.SpeechToText()
iod = iod.Devices()

# pre-config input
pci.is_text_based()
pci.see_device_list()
device_index = pci.enter_device_index()  # returns index entered
loopback = pci.is_speaker_output()  # returns true or false

# run program
running = True
while running:
    audio = stt.get_audio(is_loopback=loopback, device=device_index)
    text = stt.speech_to_text(audio_data=audio)
    stt.text_to_file(text=text, file=OUTPUT_FILE)
    message = stt.read_text(file=OUTPUT_FILE)  # this displays the last line added to the json file
    #  we can make a preliminary check here if the message is a query like time or wikipedia (future feature?)
    is_query = qy.make_query(text=message)
    try:
        response = cb.chatbot_response(message=message)  # gets a response from chatbot
        speech = tts.say(text=response)  # response is converted into audible speech
    except (TypeError, NameError):
        print("Nothing to parse or say...")
