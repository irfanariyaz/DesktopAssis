import time
import os

import speech_recognition as sr #convert speech to text
import datetime #for fetching date and time
import wikipedia
import webbrowser
import requests
from playsound import playsound # to play saved mp3 file
from gtts import gTTS # google text to speech
import os # to save/open files
import wolframalpha # to calculate strings into formula
from selenium import webdriver # to control browser operations



def talk():
    input = sr.Recognizer()
    with sr.Microphone() as source:
        audio = input.listen(source)
        data = ''
        try:
            data = input.recognize_google(audio)
            print('Your question is ,' + data)
        except sr.UnknownValueError:
            print("sorry i did not hear your question")

    return data


def respond(output):
    num = 0
    print(output)
    num +=1
    response = gTTS(text = output, lang='en')
    file = str(num) + '.mp3'
    response.save(file)
    playsound(file,True)
    os.remove(file)

if __name__ == '__main__':
    respond('Hi I am ippi your personal assistant')

    while(1):
        respond('How can I help you?')
        text = talk().lower()

        if text == 0:
            continue

        if 'stop' in str(text) or 'exit' in str(text) or 'Bye' in str(text):
            respond('ok bye take care')

        if 'wikipedia' in text:
            respond('Searching Wikipedia')
            text = text.replace('wikipedia','')
            results = wikipedia.summary(text,sentences = 3)
            respond('According to  Wikipedia')
            print(results)
            respond(results)

        elif 'time' in text:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            respond(f'the time is {strTime}')

        elif 'search' in text:
            text = text.replace('search','')
            webbrowser.open_new_tab(text)
            time.sleep(5)

        elif 'calculate' or 'what is' in text:
            question = talk()
            app_id ='Mention your API Key'
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            respond('the answer is ' +answer)

        elif 'open google' in text:
            webbrowser.open_new_tab('https://www.google.com')
            respond('Google is open')
            time.sleep(5)

        elif 'youtube ' in text:
            driver = webdriver.chrome(r'C:\Program Files\Google\Chrome\Application\chrome.exe')
            driver.implicitly_wait(1)
            driver.maximize_window()
            respond('Opening in youtube')
            indx = text.split().index('youtube')
            query = text.split()[indx + 1:]
            driver.get('https://www.youtube.com/results?search_query=' + '+'.join(query))

        elif 'open word' in text:
            respond('Opening microsoft word')
            os.startfile('Mention location  of word in your system')

        else:
            respond('Application not available')




