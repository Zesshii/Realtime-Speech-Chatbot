# Realtime-Speech-Chatbot
This program takes microphone input in which a chatbot outputs an appropriate response.

Current version is able to take microphone input, convert that input into text, save that text into json file, and output the text to the user.
In addition, that text is then processed through an intent-based Chatbot which outputs an appropriate text response. 

TO DO:
1) Create speech to text program that takes user speech and converts it to text. **COMPLETED**
   - Be able to take speaker output **PARTIALLY SOLVED** (is reliant on setting your input to microphone array)
   - Perhaps instead of using stereo mix as the input for our device speakers we instead,
     open a stream of our desktop audio using pyaudio and listen to that instead.
     if that doesn't work, perhaps attempt to setup a virtual input device using voicemeeter. **UNSOLVED**

2) Create Chatbot that takes text as input and outputs a text response **COMPLETED**
 
3) Get the Chatbot output and input that through a text to speech program **INCOMPLETE**
