from PIL import Image
import pytesseract

#print(pytesseract.image_to_string(Image.open('BG_LeGesteCreateurEtLAikido_2.jpg')))
print(pytesseract.image_to_string(open("test1.jpg", "r")))
