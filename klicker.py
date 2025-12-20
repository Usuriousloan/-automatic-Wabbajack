import pyautogui
import time
import os

BUTTON_IMAGE = 'knopka.png'

print("=== NEXUS PREMIUM 2G ENABLED ===")
print(f"SEARCHING FILE {BUTTON_IMAGE}...")

if not os.path.exists(BUTTON_IMAGE):
    print(f"ERROR: NOT FOUND {BUTTON_IMAGE}!")
    print('Make a screenshot of "Slow download", name it "button"/"knopka" (.png format) and put it in this folder with your script.')
    exit()

print("File found. Starting scanning monitor (Ctrl+C to stop)...")

while True:
    try:
        button_location = pyautogui.locateOnScreen(BUTTON_IMAGE, confidence=0.8, grayscale=True)
        
        if button_location:
            print(f"FOUND BUTTON, *CLICK*...")
            button_center = pyautogui.center(button_location)
            pyautogui.click(button_center)
            time.sleep(4)
        else:
            time.sleep(1)
            
    except Exception as e:
        print(f"Scanning... {e}")
        time.sleep(1)