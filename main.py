import speech_to_text as stt
import get_input_output_devices as iod
import chatbot as cb

"""
    ** STT Chatbot **
    this program listens for audio input from your default microphone
    and converts that audio into text
    which is then stored into the OUTPUT_FILE
    that text is read and processed by the chatbot who will output a response
    https://www.youtube.com/watch?v=1lwddP0KUEg
    ==========================================================================
    a) You must configure your sound devices to the following:
        ** Windows 11 Setup **
        1. In system -> sound settings your input device must be set to microphone array.
        2. Now, enable stereo mix by going to system -> sound -> all sound devices.
        3. Select stereo mix and press "Allow".

        ** Windows 10 Setup **
        1. Right-click the Sound icon at the right corner of Windows taskbar and click Sounds option.
        2. Click Recording tab and you can see Stereo Mix of Realtek Audio.
        3. Right-click Stereo Mix --> Enable. Click Apply and click OK to enable Realtek Stereo Mix in Windows 10.

    b) Now, define the OUTPUT_FILE and DEVICE_INDEX:
        1. OUTPUT_FILE must be the file location of a file in .json format.
        2. To find your DEVICE_INDEX run this command in terminal:
        python -c 'import speech_recognition as sr; print(sr.Microphone.list_microphone_names())' 
        3. The device you want is 'Microphone Array (something, 'Stereo Mix (Realtek(R) Audio)'

    TO DO:
        -When we want to use our speakers as input
            Perhaps instead of using stereo mix as the input for our device speakers we instead,
            Open a stream of our desktop audio using pyaudio and listen to that instead.
            If that doesn't work, perhaps attempt to setup a virtual input device using voicemeeter.
        -Create Chatbot that takes text as input
        -Get the Chatbot output and input that through a text to speech program
"""

OUTPUT_FILE = "speech.json"  # must be json file

stt = stt.SpeechToText()
iod = iod.Devices()

# ask user if they want to enter the text-based chatbot
text_based_choice = input("Do you want to use the text-based chatbot? (Y/N): ").lower()
if text_based_choice == "y":
    cb.chatbot_debug()

# ask user if they want to see list of available input devices
look_devices = input("Do you want to see a list of available devices? (Y/N): ").lower()
if look_devices == "y":
    iod.get_devices()

device_index = int(input("\nEnter the device index: "))

# ask user if using speakers as input
loopback = False
is_loopback = input("\nDo you want to use loopback to record from speakers? (Y/N): ").lower()
if is_loopback == "y":
    loopback = True

# run program
running = True
while running:
    audio = stt.get_audio(is_loopback=loopback, device=device_index)
    text = stt.speech_to_text(audio_data=audio)
    stt.text_to_file(text=text, file=OUTPUT_FILE)
    message = stt.read_text(file=OUTPUT_FILE)  # this displays the last line added to the json file
    response = cb.chatbot_response(message=message)

# now we need to input this text into the NLP program


