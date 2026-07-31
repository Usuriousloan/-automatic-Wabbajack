import pyautogui
import time
import os

BUTTON_IMAGES = ['knopka2.png', 'knopka.png']

print("=== NEXUS MULTI-BUTTON AUTOCLICKER ===")

for img in BUTTON_IMAGES:
    if os.path.exists(img):
        print(f"[OK] Файл {img} знайдено.")
    else:
        print(f"[!] Файл {img} не знайдено в папці.")

print("\nСканування екрана розпочато (Ctrl+C для зупинки)...")

while True:
    try:
        clicked = False
        
        for img in BUTTON_IMAGES:
            if not os.path.exists(img):
                continue
            
            button_location = pyautogui.locateOnScreen(img, confidence=0.75, grayscale=False)
            
            if button_location:
                print(f"ЗНАЙДЕНО: {img} -> КЛІК!")
                button_center = pyautogui.center(button_location)
                pyautogui.click(button_center)
                clicked = True
                time.sleep(3)
                break 

        if not clicked:
            time.sleep(1)

    except Exception as e:
        print(f"Scanning... {e}")
        time.sleep(1)
