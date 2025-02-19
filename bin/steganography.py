import subprocess
import sys
import importlib.util

def check_and_install_dependencies():
    required_packages = {
        'opencv-python': 'cv2',
        'numpy': 'numpy',
        'tkinter': 'tkinter'
    }
    
    missing_packages = []
    
    for package, import_name in required_packages.items():
        if package != 'tkinter':  # tkinter comes with Python
            if importlib.util.find_spec(import_name) is None:
                missing_packages.append(package)
    
    if missing_packages:
        print("Installing missing dependencies...")
        for package in missing_packages:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print(f"Successfully installed {package}")
            except subprocess.CalledProcessError:
                print(f"Failed to install {package}")
                sys.exit(1)
        print("All dependencies installed successfully!")

# Check dependencies before importing
check_and_install_dependencies()

# Original imports
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from functools import partial

def encrypt_decrypt(text, password):
    return bytes([t ^ password[i % len(password)] for i, t in enumerate(text)])

def encode_text(image_path, text, output_path, password=None):
    try:
        if password:
            text = encrypt_decrypt(text.encode(), password.encode())
        else:
            text = text.encode()
        
        text += b"====="
        data = np.frombuffer(text, dtype=np.uint8)
        
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Image not found")
        
        # Convert data to bits
        bits = np.unpackbits(data).astype(np.uint8)
        required_pixels = len(bits) // 3 + 1
        
        if img.size < required_pixels:
            raise ValueError(f"Image too small, needs at least {required_pixels} pixels")
            
        # Flatten image and embed bits in LSB
        img_flat = img.reshape(-1)
        for i in range(len(bits)):
            img_flat[i] = (img_flat[i] & 0xFE) | bits[i]
        
        cv2.imwrite(output_path, img)
        return True
    except Exception as e:
        return str(e)

def decode_text(image_path, password=None):
    try:
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Image not found")
            
        # Extract LSB from flattened image array
        img_flat = img.reshape(-1)
        bits = (img_flat & 1).astype(np.uint8)
        
        # Convert bits to bytes
        bytes_data = np.packbits(bits)
        delimiter = b"====="
        
        # Find delimiter in byte stream
        byte_list = bytes_data.tobytes()
        delim_index = byte_list.find(delimiter)
        
        if delim_index == -1:
            return "No hidden message found"
            
        encrypted_data = byte_list[:delim_index]
        
        if password:
            decrypted = encrypt_decrypt(encrypted_data, password.encode())
            return decrypted.decode()
        return encrypted_data.decode()
    except Exception as e:
        return str(e)

class SteganographyApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Steganography")
        
        # Input Image
        tk.Label(master, text="Input Image:").grid(row=0, column=0, sticky="w")
        self.input_entry = tk.Entry(master, width=40)
        self.input_entry.grid(row=0, column=1)
        tk.Button(master, text="Browse", command=self.browse_input).grid(row=0, column=2)
        
        # Output Image
        tk.Label(master, text="Output Image:").grid(row=1, column=0, sticky="w")
        self.output_entry = tk.Entry(master, width=40)
        self.output_entry.grid(row=1, column=1)
        tk.Button(master, text="Browse", command=self.browse_output).grid(row=1, column=2)
        
        # Secret Text
        tk.Label(master, text="Secret Text:").grid(row=2, column=0, sticky="w")
        self.text_entry = tk.Text(master, height=5, width=35)
        self.text_entry.grid(row=2, column=1, columnspan=2)
        
        # Password
        tk.Label(master, text="Password (optional):").grid(row=3, column=0, sticky="w")
        self.password_entry = tk.Entry(master, show="*", width=35)
        self.password_entry.grid(row=3, column=1, columnspan=2)
        
        # Buttons
        tk.Button(master, text="Encode", command=self.encode).grid(row=4, column=1, pady=10)
        tk.Button(master, text="Decode", command=self.decode).grid(row=4, column=2, pady=10)
    
    def browse_input(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, path)
    
    def browse_output(self):
        path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, path)
    
    def encode(self):
        input_path = self.input_entry.get()
        output_path = self.output_entry.get()
        text = self.text_entry.get("1.0", tk.END).strip()
        password = self.password_entry.get() or None
        
        if not all([input_path, output_path, text]):
            messagebox.showerror("Error", "All fields are required")
            return
            
        result = encode_text(input_path, text, output_path, password)
        if result is True:
            messagebox.showinfo("Success", "Message encoded successfully!")
        else:
            messagebox.showerror("Error", result)
    
    def decode(self):
        input_path = self.input_entry.get()
        password = self.password_entry.get() or None
        
        if not input_path:
            messagebox.showerror("Error", "Input image is required")
            return
            
        result = decode_text(input_path, password)
        self.text_entry.delete("1.0", tk.END)
        self.text_entry.insert("1.0", result)

if __name__ == "__main__":
    root = tk.Tk()
    app = SteganographyApp(root)
    root.mainloop()
