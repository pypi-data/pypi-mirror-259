import wikipedia

def search(search):
    result = wikipedia.summary(search, sentences = 3)
    return result