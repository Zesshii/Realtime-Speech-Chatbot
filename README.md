# Realtime-Speech-Chatbot
This program takes microphone input in which a chatbot outputs an appropriate response.

Current version is able to take microphone input, convert that input into text, save that text into json file, and output the text to the user.
In addition, that text is then processed through an intent-based Chatbot which outputs an appropriate text or speech response.

# SETUP
a) You must configure your sound devices to the following:
        ** Windows 11 Setup **
        1. In system -> sound settings your input device must be set to microphone array.
        2. Now, enable stereo mix by going to system -> sound -> all sound devices.
        3. Select stereo mix and press "Allow".

        ** Windows 10 Setup **
        1. Right-click the Sound icon at the right corner of Windows taskbar and click Sounds option.
        2. Click Recording tab and you can see Stereo Mix of Realtek Audio.
        3. Right-click Stereo Mix --> Enable. Click Apply and click OK to enable Realtek Stereo Mix in Windows 10.

    b) Now, define the OUTPUT_FILE and find your DEVICE_INDEX:
        1. OUTPUT_FILE must be the file location of a file in .json format.
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
