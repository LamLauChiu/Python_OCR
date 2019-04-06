# https://github.com/tesseract-ocr/tesseract

# https://www.youtube.com/watch?v=kxHp5ng6Rgw
from PIL import Image
import pytesseract
im = Image.open("test.png")
text = pytesseract.image_to_string(im, lang="eng")
print(text)

