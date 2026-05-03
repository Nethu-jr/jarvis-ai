import pyautogui
import pytesseract
import cv2

# ✅ IMPORTANT: Your correct Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\nethu\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# 📸 Capture screen
def capture_screen():
    img = pyautogui.screenshot()
    img.save("screen.png")

# 🔍 Extract text (IMPROVED VERSION)
def extract_text():
    # Read image in grayscale
    img = cv2.imread("screen.png", 0)

    # 🧠 Improve image quality
    img = cv2.GaussianBlur(img, (5, 5), 0)

    # Convert to black & white (threshold)
    _, img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

    # OCR
    text = pytesseract.image_to_string(img)

    return text