import pyautogui
import pydirectinput
import pygetwindow as gw
import os
from pyautogui import scroll
import time
from PIL import Image
import numpy as np

# asking for the ID
id = input("Enter the ID: ")
n_screenshots = int(input("Enter the number of screenshots: "))
image_axis = input("Enter the letter 'a' for axial or 's' for sagittal")

# determine the folder path where screenshots will be saved
folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), id)

# create the folder if it doesn't exist
os.makedirs(folder_path, exist_ok=True)

# print("Switch to the window you want to capture within the next 5 seconds...")
# time.sleep(5)  # wait for 5 seconds

# get the currently active window
# window = gw.getActiveWindow()
# Iterate through all windows and find the one with a title starting with "Change"
target_window = None
for window in gw.getAllTitles():
    if window.startswith("Change"):
        target_window = gw.getWindowsWithTitle(window)[0]
        break


if target_window is None:
    print("No active window found. Please make sure the window is open and active.")
    exit(1)

# set counter for file naming
counter = 1

def crop_image(screenshot):
    screenshot = np.array(screenshot)
    # Convert the screenshot to a Pillow Image
    pil_image = Image.fromarray(screenshot)

    # Define the specific region coordinates within the image to crop
    crop_left = 700  # Replace with your specific left coordinate
    crop_top = 400   # Replace with your specific top coordinate
    crop_width = 1200  # Replace with your specific width
    crop_height = 1000  # Replace with your specific height

    # Crop the image
    cropped_image = pil_image.crop((crop_left, crop_top, crop_left + crop_width, crop_top + crop_height))

    return cropped_image


# screenshot and scroll until end
while counter<=n_screenshots:
    try:
        

        # take a screenshot of the specific window
        # Activate the target window
        target_window.activate()
        target_window.maximize()
        # wait for the image to load
        time.sleep(0.2)
        #TODO screenshot= pyautogui.screenshot(region=(target_window.left, target_window.top, target_window.width, target_window.height))
        screenshot = pyautogui.screenshot()

        screenshot = crop_image(screenshot)
        # save the screenshot 
        screenshot.save(os.path.join(folder_path, f"{image_axis}_{id}_{counter}.png"))
        print(f'Saved {id}_{counter}.png')

        # increment the counter
        counter += 1

        # scroll down
        pydirectinput.keyDown('up')
        
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        break
