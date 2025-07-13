# Requirements:
# pip install pyautogui psutil

import pyautogui
import psutil
import random
import time

# Configuration
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
MOVE_INTERVAL = 5       # Seconds between each movement
CLICK_EVERY = 5         # Click after every N moves
CLICK_TYPES = ['left', 'middle', 'right']
Y_MIN, Y_MAX = 120, SCREEN_HEIGHT - 48  # Leave space for taskbar

def random_coordinates():
    x = random.randint(0, SCREEN_WIDTH - 1)
    y = random.randint(Y_MIN, Y_MAX)
    return x, y

def perform_random_click(x, y):
    click_type = random.choice(CLICK_TYPES)
    if click_type == 'left':
        pyautogui.leftClick(x, y)
        print(f"Left click at ({x}, {y})")
    elif click_type == 'middle':
        pyautogui.middleClick(x, y)
        print(f"Middle click at ({x}, {y})")
    elif click_type == 'right':
        pyautogui.rightClick(x, y)
        time.sleep(2)
        pyautogui.rightClick(x, y)
        print(f"Right double click at ({x}, {y})")

def main():
    move_count = 0
    print("Starting fake mouse movement. Press CTRL+C to stop.")
    try:
        while True:
            x, y = random_coordinates()
            duration = round(random.uniform(0.5, 1.5), 2)
            pyautogui.moveTo(x, y, duration=duration)
            move_count += 1

            if move_count >= CLICK_EVERY:
                perform_random_click(x, y)
                move_count = 0

            time.sleep(MOVE_INTERVAL)
    except KeyboardInterrupt:
        print("\nStopped by user.")

if __name__ == "__main__":
    main()
