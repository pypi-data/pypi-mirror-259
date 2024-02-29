import pyttsx3
import wikipedia

voice = pyttsx3.init()

def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def multiply_numbers(num1, num2):
    return num1 * num2

def divide_numbers(num1, num2):
    return num1 / num2

def search(search):
    result = wikipedia.summary(search, sentences = 3)
    return result

def voice_search(search):
    result = wikipedia.summary(search, sentences = 3)
    voice.say(result)
    voice.runAndWait()
    return result