import win32com.client as wincl
import speech_recognition as sr
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

r = sr.Recognizer()
with sr. Microphone() as source:
    speak.Speak("Hi my amazing QUEEN, how can I help you today?")
    print("Listening...")
    audio = r.listen(source)
    print ("Thinking...")

try:
    words = r.recognize_google(audio)
    speak.Speak("Ok QUEEN, let's look for " + r.recognize_google(audio))
    wb.open ("https://www.youtube.com/results?search_query=" + words)

except sr.UknownValueError:
    print("Google Speech Recognitiont could not understand audio")
except sr.RequestError as e:
    print ("Could not connect to internet")
