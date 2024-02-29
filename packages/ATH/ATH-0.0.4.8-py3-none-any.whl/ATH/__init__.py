import pyttsx3
from googlesearch import search

voice = pyttsx3.init()

def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def multiply_numbers(num1, num2):
    return num1 * num2

def divide_numbers(num1, num2):
    return num1 / num2

def search(query):
    results = list(search(query))
    return '\n'.join(results)

def voice_search(query):
    results = list(search(query))
    for result in results:
        voice.say(result)
        voice.runAndWait()
    return '\n'.join(results)