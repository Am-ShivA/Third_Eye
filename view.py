import cv2
import pyttsx3
from PIL import Image
from pytesseract import pytesseract

camera = cv2.VideoCapture(1)

while True:
    _, image = camera.read()
    cv2.imshow('Text Detectation', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite('test.jpg', image)
        break

camera.release()
cv2.destroyAllWindows()

def tesseract():
    path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    Imagepath = 'test.jpg'
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(Imagepath))
    txt = text[:-1]

    print(txt)

    engine = pyttsx3.init()
    engine.say(txt)
    engine.setProperty("rate", 200)
    engine.runAndWait()

tesseract()


