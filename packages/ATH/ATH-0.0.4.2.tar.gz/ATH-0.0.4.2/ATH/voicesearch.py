import pyttsx3
import wikipedia

voice = pyttsx3.init()
def voice_search(search):
    result = wikipedia.summary(search, sentences = 3)
    voice.say(result)
    voice.runAndWait()
    return result