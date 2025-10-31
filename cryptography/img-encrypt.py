import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import numpy as np

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

def xor_encrypt_image():
    if not image_path:
        messagebox.showerror("Error", "Please select an image first!")
        return

    try:
        # Load image
        img = Image.open(image_path)
        img_array = np.array(img)

        # XOR operation
        key = 77 # you can change this or make it user-input
        encrypted_array = img_array ^ key

        # Convert array back to image
        encrypted_img = Image.fromarray(encrypted_array)

        # Save encrypted image
        save_path = filedialog.asksaveasfilename(
            title="Save Encrypted Image",
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png")]
        )
        if save_path:
            encrypted_img.save(save_path)
            messagebox.showinfo("Success", f"Image encrypted and saved to:\n{save_path}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

window = tk.Tk()
window.title("Image XOR Encryption")
window.geometry("450x250")

image_path = None

label = tk.Label(window, text="No image selected", wraplength=400)
label.pack(pady=20)

select_btn = tk.Button(window, text="Select Image", command=select_image)
select_btn.pack(pady=10)

encrypt_btn = tk.Button(window, text="Encrypt / Decrypt Image", command=xor_encrypt_image)
encrypt_btn.pack(pady=10)

window.mainloop()
