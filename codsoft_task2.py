import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password():
    length = length_entry.get()
    complx= cmplx_entry.get()
    if not length.isdigit() or int(length) <= 0:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number.")
        return
    
    length = int(length)
    asc = string.ascii_letters  
    numbers=string.digits  
    special=string.punctuation
    if complx=="1":
        characters=asc
        password=''.join(random.choice(characters) for _ in range(length))
    if complx=="2":
        characters=asc+numbers
        password = ''.join(random.choice(characters) for _ in range(length))
    if complx=="3":
        characters=asc+numbers+special
        password=''.join(random.choice(characters)for _ in range(length))    
    result_label.config(text=password)


root = tk.Tk()
root.title("Password Generator")
root.geometry("300x300")

length_label = tk.Label(root, text="Enter password length:",background="yellow")
length_label.pack(pady=10)


length_entry = tk.Entry(root)
length_entry.pack(pady=5)

cmplx_label=tk.Label(root,text="Complexity Required: 1 or 2 or 3",bg="yellow")
cmplx_label.pack(pady=10)

cmplx_entry=tk.Entry(root)
cmplx_entry.pack(pady=5)


generate_button = tk.Button(root, text="Generate Password", command=generate_password,background="white")
generate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)


root.mainloop()
