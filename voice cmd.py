import speech_recognition as sr
import os
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)

while True:
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='hi')
        print(f"User said: {query}\n")
        if 'shutdown' in query:
            os.system('shutdown /s /t 1')
        else:
            os.system('shutdown /r /t 1')

    except Exception:
        # print(e)
        print("Say that again please...")


