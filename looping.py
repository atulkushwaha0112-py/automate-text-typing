import pyautogui
import time

messages = ["Subscribe to my channel", "Like this video", "Share with friends"]

print("Typing will start in 10 seconds...")
time.sleep(10)

for message in messages:
    for _ in range(3):
        pyautogui.write(message)
        pyautogui.press('enter')
        time.sleep(0.5)
