from  PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

image = Image.open('test1.jpg')
image.load()

# print(image)
# try:
print(pytesseract.image_to_string(image))
# except UnicodeDecodeError as unierror:
#     print("character error", unierror)
