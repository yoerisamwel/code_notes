import pytesseract
from PIL import Image

# Load the image from file
image_path = r'C:\Users\yoeri.samwel\OneDrive - DSV\Desktop\Code snippets py charm\snippets to code\1711303632594.jpg'
image = Image.open(image_path)

# Use tesseract to do OCR on the image
text = pytesseract.image_to_string(image)

text