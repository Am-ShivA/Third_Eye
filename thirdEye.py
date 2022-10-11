import pyttsx3
import wikipedia
import speech_recognition as sr
import datetime
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, None, 3)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print("You said : ", query)

    except Exception as e:
        speak("Say That Again Please...")
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    speak("Welcome to, 3rd - Eye . How may I assist you?")
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Just wait a second. Searching.")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'stop' in query:
            speak("Thank You for using me.")
            exit()


        elif 'summary' in query:
            speak("Opening, Summarizer")
            cmd = 'python summary.py'
            p = subprocess.Popen(cmd, shell=True)
            out, err = p.communicate()
            print(err)

        elif 'view' in query:
            speak("Opening, Read That, Text")
            cmd='python view.py'
            p = subprocess.Popen(cmd, shell=True)
            out,err = p.communicate()
            print(err)

        elif 'identifier' in query:
            speak("Opening, Identifier")
            cmd = 'python identifier.py'
            p = subprocess.Popen(cmd, shell=True)
            out, err = p.communicate()
            print(err)


        elif 'text' in query:
            cmd = 'python text.py'
            p = subprocess.Popen(cmd, shell=True)
            out, err = p.communicate()
            print(err)

        elif query != "None":
            speak("Sorry, I am still learning.")

