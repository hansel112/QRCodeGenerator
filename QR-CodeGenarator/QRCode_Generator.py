#!/usr/bin/env python3

"""A python script for a QR Code generator.

"""
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import qrcode
from PIL import Image, ImageTk
import io

# create the QR Code generator class with the functions.
class QRCodeGenerator:
    def __init__(self, master):
        self.master = master
        master.title("QR Code Generator")
        master.geometry("400x500")

        self.label = ttk.Label(master, text="Enter text for QR code:")
        self.label.pack(pady=10)

        self.text_entry = ttk.Entry(master, width=40)
        self.text_entry.pack(pady=10)

        self.generate_button = ttk.Button(master, text="Generate QR Code", command=self.generate_qr)
        self.generate_button.pack(pady=10)

        self.save_button = ttk.Button(master, text="Save QR Code", command=self.save_qr, state=tk.DISABLED)
        self.save_button.pack(pady=10)

        self.qr_image = ttk.Label(master)
        self.qr_image.pack(pady=10)

        self.qr_img = None  # To store the PIL Image object


# create the function for generating the QR Code
    def generate_qr(self):
        text = self.text_entry.get()
        if not text:
            messagebox.showerror("Error", "Please enter some text")
            return

        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(text)
        qr.make(fit=True)
        self.qr_img = qr.make_image(fill_color="black", back_color="white")


        # Convert the PIL image to a format Tkinter can use
        img_tk = ImageTk.PhotoImage(self.qr_img)

        self.qr_image.config(image=img_tk)
        self.qr_image.image = img_tk  # Keep a reference to avoid garbage collection

        self.save_button.config(state=tk.NORMAL)  # Enable the save button


# create the function for saving the QR Code
    def save_qr(self):
        if self.qr_img:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if file_path:
                self.qr_img.save(file_path)
                messagebox.showinfo("Success", f"QR Code saved as {file_path}")
        else:
            messagebox.showerror("Error", "No QR Code generated yet")


if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGenerator(root)
    root.mainloop()
    
    
    
