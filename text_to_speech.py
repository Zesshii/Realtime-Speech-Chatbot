import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def say(text):  # variable name shortcut
    engine.say(text)
    engine.runAndWait()
