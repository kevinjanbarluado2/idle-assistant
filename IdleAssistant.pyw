import pyautogui
import keyboard
import random
import time
import threading
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw
import os
import sys

# Flag to control the script running state
running = True

def random_mouse_movement():
    """Randomly move the mouse every few seconds."""
    screen_width, screen_height = pyautogui.size()
    while running:
        x = random.randint(0, screen_width - 1)
        y = random.randint(0, screen_height - 1)
        pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.5))
        time.sleep(random.uniform(1, 5))

def random_alt_tab():
    """Randomly perform Alt+Tab."""
    while running:
        pyautogui.hotkey('alt', 'tab')
        time.sleep(random.uniform(10, 30))

def random_ctrl_tab():
    """Randomly perform Ctrl+Tab."""
    while running:
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(random.uniform(15, 45))

def random_keystrokes():
    """Randomly perform keystrokes."""
    keys = ['a', 's', 'd', 'f', 'q', 'w', 'e', 'r', 't', 'y', '1', '2', '3', '4', 'space']
    while running:
        random_key = random.choice(keys)
        pyautogui.press(random_key)
        time.sleep(random.uniform(5, 15))

def monitor_exit():
    """Monitors for the ESC key press to exit the script."""
    global running
    while running:
        if keyboard.is_pressed('esc'):
            running = False
            break
        time.sleep(0.1)

def stop_script(icon, item):
    """Stop the script and exit."""
    global running
    running = False
    icon.stop()

def restart_script(icon, item):
    """Restart the script."""
    global running
    running = False
    icon.stop()
    
    # Restart the script
    os.execv(sys.executable, ['python'] + sys.argv)

def setup_tray_icon():
    """Create a system tray icon."""
    # Load the icon image from file
    icon_image = Image.open("./icon.png")  

    # Create a menu for the tray icon with Exit and Restart options
    menu = Menu(
        MenuItem('Restart', restart_script),  # Add Restart option
        MenuItem('Exit', stop_script)         # Add Exit option
    )

    # Create the tray icon
    icon = Icon("Idle Assistant", icon_image, "Idle Assistant", menu)

    return icon

def start_background_tasks():
    """Start background tasks."""
    # Threads for each task
    mouse_thread = threading.Thread(target=random_mouse_movement)
    alt_tab_thread = threading.Thread(target=random_alt_tab)
    ctrl_tab_thread = threading.Thread(target=random_ctrl_tab)
    keystrokes_thread = threading.Thread(target=random_keystrokes)
    exit_thread = threading.Thread(target=monitor_exit)

    # Start all threads
    mouse_thread.start()
    alt_tab_thread.start()
    ctrl_tab_thread.start()  # Start Ctrl+Tab thread
    keystrokes_thread.start()
    exit_thread.start()

    # Wait for all threads to finish
    mouse_thread.join()
    alt_tab_thread.join()
    ctrl_tab_thread.join()  # Wait for Ctrl+Tab thread
    keystrokes_thread.join()
    exit_thread.join()

# Main function to run the tray icon and background tasks
def main():
    # Setup the system tray icon
    tray_icon = setup_tray_icon()

    # Start the background tasks in a separate thread
    background_thread = threading.Thread(target=start_background_tasks)
    background_thread.start()

    # Run the system tray icon (this will block until the icon is stopped)
    tray_icon.run()

if __name__ == "__main__":
    main()
