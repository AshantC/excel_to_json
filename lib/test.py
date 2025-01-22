import pyautogui
import time
import keyboard  # To detect keypresses

def move_cursor():
    print("Starting cursor movement... Press 'Esc' to exit.")
    time.sleep(2)  # Delay before starting

    # Get the screen size
    screen_width, screen_height = pyautogui.size()
    print(f"Screen resolution: {screen_width}x{screen_height}")

    steps = 200  # Distance to move in each direction

    # Infinite loop to keep moving the cursor until 'Esc' is pressed
    while True:
        # Check if 'Esc' key is pressed
        if keyboard.is_pressed("esc"):
            print("Exiting program...")
            break

        # Move cursor in a square pattern
        pyautogui.move(steps, 0, duration=1)  # Move right
        time.sleep(1 * 60)
        pyautogui.move(0, steps, duration=1)  # Move down
        time.sleep(1 * 60)
        pyautogui.move(-steps, 0, duration=1)  # Move left
        time.sleep(1 * 60)
        pyautogui.move(0, -steps, duration=1)  # Move up
        time.sleep(1 * 60)

        print("Completed one loop of movement. Continuing...")

if __name__ == "__main__":
    move_cursor()
