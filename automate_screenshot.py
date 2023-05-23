import pyautogui
import pygetwindow as gw
import os
from pyautogui import scroll
import time

# asking for the ID
id = input("Enter the ID: ")

# determine the folder path where screenshots will be saved
folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), id)

# create the folder if it doesn't exist
os.makedirs(folder_path, exist_ok=True)

print("Switch to the window you want to capture within the next 5 seconds...")
time.sleep(5)  # wait for 5 seconds

# get the currently active window
window = gw.getActiveWindow()

if window is None:
    print("No active window found. Please make sure the window is open and active.")
    exit(1)

# set counter for file naming
counter = 1

# screenshot and scroll until end
while counter<50:
    try:
        # take a screenshot of the specific window
        # TODO: region=(window.left, window.top, window.width, window.height)
        screenshot = pyautogui.screenshot()

        # save the screenshot
        screenshot.save(os.path.join(folder_path, f"{id}_{counter}.png"))
        print(f'Saved {id}_{counter}.png')

        # increment the counter
        counter += 1

        # scroll down
        #window.activate()  # ensure the window is active
        #scroll(clicks=-1, _pause = False)
        pyautogui.press('up', _pause = False, interval=0.1)
        # wait for the scroll
        # time.sleep(0.1)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        break
