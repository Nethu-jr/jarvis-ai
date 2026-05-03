from voice import speak, take_command
from screen import capture_screen, extract_text
from ai_brain import ask_ollama
import automation

speak("Jarvis AI ready")

while True:
    command = take_command()

    print("Command:", command)

    # 🔍 AI SCREEN ANALYSIS
    if "screen" in command or "analyze" in command or "what is this" in command:
        speak("Analyzing your screen")

        capture_screen()
        text = extract_text()

        if text.strip():
            speak("Thinking...")
            answer = ask_ollama(text)
            speak(answer)
        else:
            speak("No text found")

    # 🌐 OPEN WEBSITE (ANY WEBSITE)
    elif "open" in command and "app" not in command:
        speak("Opening")
        site = command.replace("open", "").strip()
        automation.open_website(site)

    # 💻 OPEN ANY APP
    elif "open app" in command:
        speak("Opening app")
        app = command.replace("open app", "").strip()
        automation.open_app(app)

    # 📂 OPEN FILE/FOLDER
    elif "open file" in command:
        speak("Opening file")
        path = command.replace("open file", "").strip()
        automation.open_file(path)

    # ❌ CLOSE WINDOW
    elif "close window" in command or "close" in command:
        speak("Closing")
        automation.close_window()

    # 🖱️ SCROLL
    elif "scroll down" in command:
        automation.scroll_down()

    elif "scroll up" in command:
        automation.scroll_up()

    # 🖱️ CLICK
    elif "click" in command:
        automation.click()

    # ⌨️ TYPE
    elif "type" in command:
        speak("What should I type?")
        text = take_command()
        automation.type_text(text)

    else:
        print("Waiting...")