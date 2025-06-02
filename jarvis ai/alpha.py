import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import sys
from urllib.parse import quote_plus          # for URL‑encoding

# ───────────── Text‑to‑speech setup ──────────────────────────────
engine = pyttsx3.init()                      # auto‑detect driver (sapi5 on Win)
voices = engine.getProperty("voices")
if voices:
    engine.setProperty("voice", voices[0].id)   # 0 = first voice (usually male)

def speak(text: str) -> None:
    engine.say(text)
    engine.runAndWait()

# ───────────── Helper functions ──────────────────────────────────
def log(text: str) -> None:
    """Print what Jarvis heard, with timestamp (ASCII‑safe)."""
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] You said -> {repr(text)}")

def wish_me() -> None:
    hour = datetime.datetime.now().hour
    if hour < 12:
        greet = "Good morning!"
    elif hour < 18:
        greet = "Good afternoon!"
    else:
        greet = "Good evening!"
    speak(f"{greet} I am Jarvis. Please tell me how may I help you.")

def take_command() -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening…")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language="en-in")
        log(query)                       # print to terminal
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not catch that.")
    except sr.RequestError:
        speak("Speech‑recognition service is unavailable.")
    return ""

def send_email(to: str, content: str) -> None:
    # Use an app password or OAuth2 for production
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("youremail@gmail.com", "your-password")
        server.sendmail("youremail@gmail.com", to, content)

# ───────────── Core command executor ─────────────────────────────
def execute(query: str) -> None:
    if not query:
        return

    # —— Wikipedia ——
    if "wikipedia" in query:
        speak("Searching Wikipedia…")
        topic = query.replace("wikipedia", "").strip() or "Wikipedia"
        try:
            result = wikipedia.summary(topic, sentences=2)
            speak("According to Wikipedia")
            speak(result)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("Be more specific. Options include " + ", ".join(e.options[:5]))
        except wikipedia.exceptions.PageError:
            speak("No page found for that topic.")

    # —— YouTube search (URL‑encoded) ——
    elif "search youtube for" in query:
        term = query.replace("search youtube for", "").strip()
        if term:
            url = f"https://www.youtube.com/results?search_query={quote_plus(term)}"
            webbrowser.open(url)
            speak(f"Searching YouTube for {term}")
        else:
            speak("What should I search for on YouTube?")

    # —— YouTube open/close ——
    elif "open youtube" in query:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif "close youtube" in query:
        os.system("taskkill /f /im chrome.exe")
        speak("Closing YouTube")

    # —— Google open/close ——
    elif "open google" in query:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif "close google" in query:
        os.system("taskkill /f /im chrome.exe")
        speak("Closing Google")

    # —— Stack Overflow open/close ——
    elif "open stackoverflow" in query:
        webbrowser.open("https://stackoverflow.com")
        speak("Opening Stack Overflow")
    elif "close stackoverflow" in query:
        os.system("taskkill /f /im chrome.exe")
        speak("Closing Stack Overflow")

    # —— Music play/stop ——
    elif "play music" in query:
        music_dir = r"D:\Non Critical\songs\Favorite Songs2"
        try:
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, songs[0]))
                speak("Playing music")
            else:
                speak("No songs found in the directory.")
        except FileNotFoundError:
            speak("Music directory not found.")
    elif "stop music" in query or "close music" in query:
        os.system("taskkill /f /im wmplayer.exe")
        speak("Stopping music")

    # —— Time ——
    elif "the time" in query:
        speak(f"The time is {datetime.datetime.now().strftime('%H:%M:%S')}")

    # —— VS Code open/close ——
    elif "open code" in query:
        code_path = r"C:\Users\Haris\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        os.startfile(code_path)
        speak("Opening VS Code")
    elif "close code" in query:
        os.system("taskkill /f /im Code.exe")
        speak("Closing VS Code")

    # —— Send email ——
    elif "send mail to rohit" in query:
        try:
            speak("What should I say?")
            content = take_command()
            if content:
                send_email("rohit@example.com", content)
                speak("Email has been sent!")
        except Exception:
            speak("Sorry, I am unable to send the email.")

    # —— ChatGPT open/close ——
    elif "open chatgpt" in query:
        webbrowser.open("https://chat.openai.com")
        speak("Opening ChatGPT")
    elif "close chatgpt" in query:
        os.system("taskkill /f /im chrome.exe")
        speak("Closing ChatGPT")

    # —— WhatsApp open/close ——
    elif "open whatsapp" in query:
        webbrowser.open("https://web.whatsapp.com")
        speak("Opening WhatsApp Web")
    elif "close whatsapp" in query:
        os.system("taskkill /f /im chrome.exe")
        speak("Closing WhatsApp")

    # —— Facebook open/close ——
    elif "open facebook" in query:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook")
    elif "close facebook" in query:
        os.system("taskkill /f /im chrome.exe")
        speak("Closing Facebook")

    # —— Instagram open/close ——
    elif "open instagram" in query:
        webbrowser.open("https://www.instagram.com")
        speak("Opening Instagram")
    elif "close instagram" in query:
        os.system("taskkill /f /im chrome.exe")
        speak("Closing Instagram")

    # —— Shutdown / restart ——
    elif "shutdown computer" in query:
        speak("Shutting down the computer")
        os.system("shutdown /s /t 1")
    elif "restart computer" in query:
        speak("Restarting the computer")
        os.system("shutdown /r /t 1")

    # —— Notepad open/close ——
    elif "open notepad" in query:
        os.startfile(r"C:\Windows\system32\notepad.exe")
        speak("Opening Notepad")
    elif "close notepad" in query:
        os.system("taskkill /f /im notepad.exe")
        speak("Closing Notepad")

    # —— Calculator open/close ——
    elif "open calculator" in query:
        os.system("calc")
        speak("Opening Calculator")
    elif "close calculator" in query:
        os.system("taskkill /f /im Calculator.exe")
        speak("Closing Calculator")

    # —— Small talk ——
    elif "what is your name" in query or "who are you" in query:
        speak("I am Jarvis, your personal assistant.")
    elif "how are you" in query:
        speak("I'm doing great, thank you for asking!")
    elif "thank you" in query or "thanks" in query:
        speak("You're welcome!")

    # —— Exit ——
    elif "exit" in query or "quit" in query or "stop jarvis" in query:
        speak("Goodbye!")
        sys.exit()

    # —— Unknown ——
    else:
        speak("I didn't understand that command. Please try again.")

# ───────────── Main loop ─────────────────────────────────────────
if __name__ == "__main__":
    wish_me()
    while True:
        command = take_command()
        execute(command)
