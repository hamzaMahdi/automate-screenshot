import pyautogui
import pydirectinput
import pygetwindow as gw
import os
from pyautogui import scroll
import time

# asking for the ID
id = input("Enter the ID: ")
n_screenshots = int(input("Enter the number of screenshots: "))

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
        # save the screenshot
        screenshot.save(os.path.join(folder_path, f"{id}_{counter}.png"))
        print(f'Saved {id}_{counter}.png')

        # increment the counter
        counter += 1

        # scroll down
        pydirectinput.keyDown('up')
        
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        break
