import speech_to_text as stt

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
        Create Chatbot that takes text as input
        Get the Chatbot output and input that through a text to speech program
"""

OUTPUT_FILE = "C:/Users/dylan/PycharmProjects/SpeechToText/speech.json"  # must be json file
DEVICE_INDEX = 2

stt = stt.SpeechToText()

# ask user if using speakers as input
loopback = False
is_loopback = input("Do you want to use loopback to record from speakers? (Y/N): ").lower()
if is_loopback == "y":
    loopback = True

# run program
running = True
while running:
    audio = stt.get_audio(is_loopback=loopback, device=DEVICE_INDEX)
    text = stt.speech_to_text(audio_data=audio)
    stt.text_to_file(text=text, file=OUTPUT_FILE)
    stt.read_text(file=OUTPUT_FILE)  # this displays the last line added to the json file

# now we need to input this text into the NLP program

