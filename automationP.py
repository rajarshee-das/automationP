import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser 
import os
import smtplib

try:
    from googlesearch import search
except ImportError:
    print("No module named google found")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning my friend")
    elif 12 <= hour < 18:
        speak("Good afternoon my friend")
    else:
        speak("Good evening my friend")
    speak("Let me know how can I help you, what are you looking for?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to you Rajarshee......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing your voice")
        query = r.recognize_google(audio, language='en-in')
        print(f"My friend, you said: {query}\n")
    except Exception as e:
        print("Rajarshee, say that again please......")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('place email id','place email password')  
    server.sendmail('rajkri2003@gmail.com',to, content)
    server.close()

if __name__ == '__main__':
    wishme()

    while True:
        a=takecommand()
        if(a!=None):
            query=a.lower().strip()
        
        if not query:
            continue
        
        if 'wikipedia' in query:
            speak('Searching wikipedia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'notepad' in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
        
        elif 'paint' in query:
            os.startfile("mspaint.exe")

        elif 'youtube' in query:
            webbrowser.open('youtube.com')

        elif 'great learning academy' in query:
            webbrowser.open("https://www.greatlearning.in/academy")

        elif 'google' in query:
            webbrowser.open("google.com")
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"My friend, the time is {strTime}")

        elif 'linkedin' in query:
            webbrowser.open("linkedin.com")

        elif 'send email' in query:
            try:
                speak("What should I send?")
                content = takecommand()
                if content:
                    to = "place destination mail id"
                    sendEmail(to, content)
                    speak("Your email has been sent successfully")
            except Exception as e:
                print(e)
                speak("My friend... I am unable to send the email...please address the error")

        elif 'stop' in query:
            speak("Thank you for using the project , have a great time ")
            break

        elif query!=None:
            speak("Please say one more time ") 
            r=sr.Recognizer()
            with sr.Microphone() as source:
                audio=r.listen(source)
            try:
                text=r.recognize_google(audio)
            except sr.UnknownValueError:
                print("What you said can not be converted into a text .")
            except sr.RequestError:
                print("Could not request results from google speech recognition service .")
            speak("You can search the thing in the given links")
            for j in search(text,tld="co.in",num=10,stop=10,pause=2):
                print(j)

        
