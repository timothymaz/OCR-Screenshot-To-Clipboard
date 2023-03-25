import pytesseract
from PIL import Image

# Set the path to the Tesseract executable (Windows only)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Open the image
image = Image.open(r'C:\Users\Tim\PasswordGen\OCR Cheat\unnamed.png')

# Perform OCR on the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
