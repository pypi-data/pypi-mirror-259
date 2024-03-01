import pyttsx3

voice = pyttsx3.init()

def tts(thing):
    voice.say(thing)
    voice.runAndWait()
    return thing