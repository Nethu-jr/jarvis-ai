import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import sys
from urllib.parse import quote_plus

# ───────────── TTS SETUP (FIXED) ─────────────
engine = pyttsx3.init('sapi5')

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

def speak(text):
    engine.stop()
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# ───────────── HELPERS ─────────────
def log(text):
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] You said -> {text}")

def wish_me():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis. How can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language="en-in")
        log(query)
        return query.lower()
    except:
        speak("Sorry, say that again.")
        return ""

# ───────────── EMAIL ─────────────
def send_email(to, content):
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("youremail@gmail.com", "your-password")
        server.sendmail("youremail@gmail.com", to, content)

# ───────────── MAIN EXECUTOR ─────────────
def execute(query):

    if not query:
        return

    # ─── Wikipedia ───
    if "wikipedia" in query:
        speak("Searching Wikipedia")
        topic = query.replace("wikipedia", "")
        try:
            result = wikipedia.summary(topic, sentences=2)
            speak(result)
        except:
            speak("No results found")

    # ─── YouTube Search ───
    elif "search youtube for" in query:
        term = query.replace("search youtube for", "").strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={quote_plus(term)}")
        speak(f"Searching YouTube for {term}")

    # ─── OPEN WEBSITES ───
    elif "open youtube" in query:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "open google" in query:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif "open whatsapp" in query:
        webbrowser.open("https://web.whatsapp.com")
        speak("Opening WhatsApp")

    elif "open chatgpt" in query:
        webbrowser.open("https://chat.openai.com")
        speak("Opening ChatGPT")

    elif "open instagram" in query:
        webbrowser.open("https://instagram.com")
        speak("Opening Instagram")

    elif "open facebook" in query:
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook")

    # ─── CLOSE WEBSITES (BROWSER) ───
    elif "close browser" in query or "close youtube" in query:
        os.system("taskkill /f /im chrome.exe")
        os.system("taskkill /f /im msedge.exe")
        speak("Closing browser")

    # ─── SYSTEM APPS ───
    elif "open file manager" in query:
        os.system("explorer")
        speak("Opening File Manager")

    elif "open settings" in query:
        os.system("start ms-settings:")
        speak("Opening Settings")

    elif "open control panel" in query:
        os.system("control")
        speak("Opening Control Panel")

    elif "open task manager" in query:
        os.system("taskmgr")
        speak("Opening Task Manager")

    elif "open cmd" in query:
        os.system("start cmd")
        speak("Opening Command Prompt")

    elif "open powershell" in query:
        os.system("start powershell")
        speak("Opening PowerShell")

    elif "open camera" in query:
        os.system("start microsoft.windows.camera:")
        speak("Opening Camera")

    elif "open paint" in query:
        os.system("mspaint")
        speak("Opening Paint")

    elif "open snipping tool" in query:
        os.system("snippingtool")
        speak("Opening Snipping Tool")

    elif "open downloads" in query:
        os.system("explorer shell:Downloads")
        speak("Opening Downloads")

    elif "open documents" in query:
        os.system("explorer shell:Documents")
        speak("Opening Documents")

    elif "open desktop" in query:
        os.system("explorer shell:Desktop")
        speak("Opening Desktop")

    elif "open recycle bin" in query:
        os.system("start shell:RecycleBinFolder")
        speak("Opening Recycle Bin")

    # ─── APPS ───
    elif "open notepad" in query:
        os.startfile("notepad.exe")
        speak("Opening Notepad")

    elif "close notepad" in query:
        os.system("taskkill /f /im notepad.exe")
        speak("Closing Notepad")

    elif "open calculator" in query:
        os.system("calc")
        speak("Opening Calculator")

    elif "close calculator" in query:
        os.system("taskkill /f /im Calculator.exe")
        speak("Closing Calculator")

    elif "open code" in query:
        os.startfile("C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        speak("Opening VS Code")

    elif "close code" in query:
        os.system("taskkill /f /im Code.exe")
        speak("Closing VS Code")

    # ─── MUSIC ───
    elif "play music" in query:
        music_dir = "D:\\Music"
        try:
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Playing music")
        except:
            speak("Music folder not found")

    elif "stop music" in query:
        os.system("taskkill /f /im wmplayer.exe")
        speak("Stopping music")

    # ─── TIME ───
    elif "time" in query:
        speak(datetime.datetime.now().strftime("%H:%M:%S"))

    # ─── SYSTEM CONTROL ───
    elif "shutdown" in query:
        speak("Shutting down")
        os.system("shutdown /s /t 1")

    elif "restart" in query:
        speak("Restarting")
        os.system("shutdown /r /t 1")

    elif "close everything" in query:
        os.system("taskkill /f /im chrome.exe")
        os.system("taskkill /f /im Code.exe")
        os.system("taskkill /f /im notepad.exe")
        speak("Closing everything")

    # ─── EXIT ───
    elif "exit" in query or "stop" in query:
        speak("Goodbye")
        sys.exit()

    else:
        speak("I didn't understand that command")

# ───────────── MAIN LOOP ─────────────
if __name__ == "__main__":
    wish_me()
    while True:
        command = take_command()
        execute(command)
