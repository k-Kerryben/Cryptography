from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image # Pillow library for image handling
import numpy as np

# pip install tk numpy pillow

def select_image():
    global image_path
    image_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )
    if image_path:
        label.config(text=f"Selected: {image_path}")
    else:
        label.config(text="No image selected")
        
def xor_encrypt_image(encrypt=True):
    global image_path
    try:
        key = int(key_entry.get()) # Get the XOR key from user input
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer key!")
        return
    # pixelvalue = 200^55 ==> encrypted pixel value = 143
    #choice = messagebox.askquestion("Encrypt or Decrypt", "Do you want to Encrypt the image? (No will Decrypt)")
    if not image_path:
        messagebox.showerror("Error", "Please select an image first!")
        return

    try:
        # Load image
        img = Image.open(image_path)
        img_array = np.array(img)
        # Apply XOR operation
        xor_array = np.bitwise_xor(img_array, key) 
        # Convert back to image
        xor_img = Image.fromarray(xor_array.astype('uint8'))
        # Save the new image
        action = "encrypted" if encrypt else "decrypted"
        save_path = filedialog.asksaveasfilename(
            title=f"Save {action.capitalize()} Image as",
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg")]
        )
        if save_path:
            xor_img.save(save_path)
            messagebox.showinfo("Success", f"Image {action} and saved to:\n{save_path}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def restart_program():
    global image_path
    image_path = None
    label.config(text="No image selected")
    key_entry.delete(0, END)
    # messagebox.showinfo("Info", "Program restarted!")

window = Tk() # Create the main window
window.title("Image XOR Encryption") 
window.geometry("400x300")

image_path = None # eg C:\path\to\image.png

label = Label(window, text="No image selected", wraplength=400)
label.pack(pady=20)

key_label = Label(window, text="Enter XOR Key (0-255):")
key_label.pack() 
   
key_entry = Entry(window)
key_entry.pack(pady=5)

select_btn = Button(window, text="Select Image", command=select_image)
select_btn.pack(pady=10, padx=10)

encrypt_btn = Button(window, text="Encrypt Image", command=lambda: xor_encrypt_image(encrypt=True))
encrypt_btn.pack(pady=10, padx=10)

decrypt_btn = Button(window, text="Decrypt Image", command=lambda: xor_encrypt_image(encrypt=False))
decrypt_btn.pack(pady=10, padx=10)

restart_btn = Button(window, text="Restart Program", command=restart_program)
restart_btn.pack(pady=10, padx=10)

window.mainloop() #keeps the window open until the user closes it
