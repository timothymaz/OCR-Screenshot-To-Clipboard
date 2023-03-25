import pytesseract
import pyperclip
import pyscreenshot as ImageGrab
import mouse
# Set the path to the Tesseract executable (Windows only)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def sort_coordinates(x1, y1, x2, y2):
    return min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)


# Wait for the left mouse button to be pressed
mouse.wait(button='left', target_types=('down',))

# Get the starting coordinates
start_x, start_y = mouse.get_position()

# Wait for the left mouse button to be released
mouse.wait(button='left', target_types=('up',))

# Get the ending coordinates
end_x, end_y = mouse.get_position()



# Take a screenshot of the specified area
sorted_coordinates = sort_coordinates(start_x, start_y, end_x, end_y)
screenshot = ImageGrab.grab(bbox=sorted_coordinates)

# Perform OCR on the screenshot
text = pytesseract.image_to_string(screenshot)

# Copy the extracted text to the clipboard
pyperclip.copy(text)

print("Text from the selected area has been copied to the clipboard.")