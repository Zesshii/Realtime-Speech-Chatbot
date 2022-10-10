# Realtime-Speech-Chatbot
This program takes microphone input in which a chatbot outputs an appropriate response.

Current version is able to take microphone input, convert that input into text, save that text into json file, and output the text to the user.

TO DO:
1) When we want to use our speakers as input:
Perhaps instead of using stereo mix as the input for our device speakers we instead,
open a stream of our desktop audio using pyaudio and listen to that instead.
if that doesn't work, perhaps attempt to setup a virtual input device using voicemeeter. **UNSOLVED**

2) Create Chatbot that takes text as input and outputs a text response **COMPLETED**
 
3) Get the Chatbot output and input that through a text to speech program **INCOMPLETE**
