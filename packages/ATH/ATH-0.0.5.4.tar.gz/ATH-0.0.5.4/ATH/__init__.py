import pyttsx3
from msedge.selenium_tools import Edge, EdgeOptions

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
    options = EdgeOptions()
    options.use_chromium = True
    driver = Edge(options=options)
    driver.get(f"https://www.google.com/search?q={query}")
    results = driver.find_elements_by_css_selector('div.g')
    search_results = []
    for result in results[:3]:
        title = result.find_element_by_css_selector('h3').text
        url = result.find_element_by_css_selector('a').get_attribute('href')
        search_results.append(f"{title}: {url}")
    driver.quit()
    return '\n'.join(search_results)

def voice_search(query):
    results = list(search(query))
    for result in results:
        voice.say(result)
        voice.runAndWait()
    return '\n'.join(results)