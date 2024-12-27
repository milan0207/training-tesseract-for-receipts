import pytesseract
from PIL import Image

img= Image.open(r"D:\Egyetem\Egyetem_3.1\Allamvizsga\TestKepek\test6.jpg")
text = pytesseract.image_to_string(img, lang='augSubtle',config='--psm 4')
text2=pytesseract.image_to_string(img, lang='eng',config='--psm 4')
print(text)
print(text2)