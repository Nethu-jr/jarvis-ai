import os
import webbrowser
import pyautogui
import pyperclip

# 🌐 Open websites
def open_website(name):
    try:
        webbrowser.open(f"https://{name}.com")
    except:
        print("Error opening website")

# 💻 Open apps
def open_app(app):
    try:
        os.system(f"start {app}")
    except:
        print("Error opening app")

# 📂 Open files/folders
def open_file(path):
    try:
        os.startfile(path)
    except:
        print("Error opening file")

# ❌ Close current window
def close_window():
    pyautogui.hotkey("alt", "f4")

# 🖱️ Scroll
def scroll_down():
    pyautogui.scroll(-800)

def scroll_up():
    pyautogui.scroll(800)

# 🖱️ Click
def click():
    pyautogui.click()

# ⌨️ Type text
def type_text(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")