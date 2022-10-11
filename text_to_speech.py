import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 150)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)
engine.say("hello I am the voice from your PC")
engine.runAndWait()

