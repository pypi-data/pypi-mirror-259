import pyttsx3

voice = pyttsx3.init()

def say(thing):
    voice.say(thing)
    voice.runAndWait()