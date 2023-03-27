import pytesseract
import pyperclip
import clipboard
import pyscreenshot as ImageGrab
import keyboard
import tkinter as tk
import os


def sort_coordinates(x1, y1, x2, y2):
    return min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)

def on_start_selection(event):
    global start_x, start_y, rectangle
    start_x, start_y = event.x, event.y
    rectangle = canvas.create_rectangle(start_x, start_y, start_x, start_y, outline='white', width=1, fill='', stipple='gray12')


def on_move_selection(event):
    global end_x, end_y
    end_x, end_y = event.x, event.y
    canvas.coords(rectangle, start_x, start_y, end_x, end_y)

def on_end_selection(event):
    root.quit()

def capture_and_ocr():
    sorted_coordinates = sort_coordinates(start_x, start_y, end_x, end_y)
    screenshot = ImageGrab.grab(bbox=(root.winfo_x() + sorted_coordinates[0],
                                       root.winfo_y() + sorted_coordinates[1],
                                       root.winfo_x() + sorted_coordinates[2],
                                       root.winfo_y() + sorted_coordinates[3]))

    text = pytesseract.image_to_string(screenshot)
    clipboard.copy(text)  # Use clipboard.copy instead of pyperclip.copy
    print(text)
    print("Text from the selected area has been copied to the clipboard.")



# Check if Tesseract is installed in the default locationI
tesseract_default_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

if os.path.exists(tesseract_default_path):
    pytesseract.pytesseract.tesseract_cmd = tesseract_default_path
else:
    # Ask the user to provide the Tesseract installation path
    tesseract_path = input("Please enter the path to the Tesseract executable: ")
    pytesseract.py


# Run indefinitely
while True:
    if keyboard.is_pressed('shift') and keyboard.is_pressed('i'):
        root = tk.Tk()
        root.attributes('-alpha', 0.3)  # Set window transparency
        root.attributes('-topmost', True)  # Keep the window on top of other windows
        root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        root.configure(background='gray')

        canvas = tk.Canvas(root, bg='black', highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)

        canvas.bind("<Button-1>", on_start_selection)
        canvas.bind("<B1-Motion>", on_move_selection)
        canvas.bind("<ButtonRelease-1>", on_end_selection)

        root.mainloop()

        capture_and_ocr()

        # Close the tkinter window
        root.destroy()

        # Wait for 'Shift' and 'i' keys to be released before checking again
        while keyboard.is_pressed('shift') or keyboard.is_pressed('i'):
            keyboard.read_event()