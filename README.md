# Realtime-Speech-Chatbot
This program takes microphone input in which a chatbot outputs an appropriate response.

Current version is able to take microphone input, convert that input into text, save that text into json file, and output the text to the user.
In addition, that text is then processed through an intent-based Chatbot which outputs an appropriate text or speech response.

# Speaker Output Setup
a) If you want speaker output as input you must configure your sound devices to the following:

**Windows 11 Setup VB-Audio Cable**
1. Download VB-Audio Cable here: https://vb-audio.com/Cable/index.htm
2. In system -> sound settings, set your input device to "Cable Output" (VB-Audio Cable)
3. Also in system -> sound settings, set your output device to "Cable Input" (VB-Audio Cable)

**Windows 11 Setup Microphone Array**
1. In system -> sound settings your input device must be set to microphone array.
2. Now, enable stereo mix by going to system -> sound -> all sound devices.
3. Select stereo mix and press "Allow".

**Windows 10 Setup Realtek Audio Stereo Mix**
1. Right-click the Sound icon at the right corner of Windows taskbar and click Sounds option.
2. Click Recording tab and you can see Stereo Mix of Realtek Audio.
3. Right-click Stereo Mix --> Enable. Click Apply and click OK to enable Realtek Stereo Mix in Windows 10.
        
b) Now, define the OUTPUT_FILE in main.py and find your device_index:
1. OUTPUT_FILE must be the file path/location of a file in .json format.
2. Run the program, and when prompted say y to see a list of devices.
5. Get the index of the Stereo Mix (Realtek(R) Audio) device.
6. Input the device index when prompted.

# TO DO:
1) Create speech to text program that takes user speech and converts it to text. **COMPLETED**
   - Be able to take speaker output **PARTIALLY SOLVED** (is reliant on setting your input to microphone array)
   - Perhaps instead of using stereo mix as the input for our device speakers we instead,
     open a stream of our desktop audio using pyaudio and listen to that instead.
     if that doesn't work, perhaps attempt to setup a virtual input device using voicemeeter. **UNSOLVED**

2) Create Chatbot that takes text as input and outputs a text response **COMPLETED**
 
3) Get the Chatbot output and input that through a text to speech program **COMPLETED**

# TO DO LATER:
1) Clean and reformat code **PENDING**
2) Program GUI **PENDING**

# Resources and Acknowledgements
- Credit to NeuralNine for the intent-based Chatbot, see his video tutorial here: https://www.youtube.com/watch?v=1lwddP0KUEg&t=450s
- SpeechRecognition git: https://github.com/Uberi/speech_recognition#readme
- Pyttsx3 docs: https://pyttsx3.readthedocs.io/en/latest/engine.html
