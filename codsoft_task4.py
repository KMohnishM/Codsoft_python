import tkinter as tk
from tkinter import simpledialog, messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

contacts = []

def add_contact(contacts_list, contact):
    contacts_list.append(contact)

def search_contact(contacts_list, search_term):
    results = [contact for contact in contacts_list if search_term.lower() in contact.name.lower() or search_term in contact.phone]
    return results

def update_contact(contact, name=None, phone=None, email=None, address=None):
    if name:
        contact.name = name
    if phone:
        contact.phone = phone
    if email:
        contact.email = email
    if address:
        contact.address = address

def delete_contact(contacts_list, contact):
    contacts_list.remove(contact)

def add_contact_ui():
    name = simpledialog.askstring("Input", "Enter name:")
    phone = simpledialog.askstring("Input", "Enter phone:")
    while len(phone) < 10:
        messagebox.showerror("Error", "Invalid phone number. Please re-enter.")
        phone = simpledialog.askstring("Input", "Enter phone:")
    email = simpledialog.askstring("Input", "Enter email:")
    address = simpledialog.askstring("Input", "Enter address:")
    contact = Contact(name, phone, email, address)
    add_contact(contacts, contact)
    messagebox.showinfo("Success", "Contact added successfully.")

def view_contacts_ui():
    details_to_show = []
    show_name = messagebox.askyesno("Show details", "Show name?")
    show_phone = messagebox.askyesno("Show details", "Show phone number?")
    show_email = messagebox.askyesno("Show details", "Show email?")
    show_address = messagebox.askyesno("Show details", "Show address?")
    
    if show_name:
        details_to_show.append('name')
    if show_phone:
        details_to_show.append('phone')
    if show_email:
        details_to_show.append('email')
    if show_address:
        details_to_show.append('address')

    contact_list_window = tk.Toplevel(root)
    contact_list_window.title("Contact List")
    contact_list_window.config(bg="#F0F8FF")
    
    for i, contact in enumerate(contacts):
        contact_details = [f"{i + 1}. "]
        if 'name' in details_to_show:
            contact_details.append(f"Name: {contact.name}")
        if 'phone' in details_to_show:
            contact_details.append(f"Phone: {contact.phone}")
        if 'email' in details_to_show:
            contact_details.append(f"Email: {contact.email}")
        if 'address' in details_to_show:
            contact_details.append(f"Address: {contact.address}")
        tk.Label(contact_list_window, text=", ".join(contact_details), bg="#F0F8FF").pack()

def search_contact_ui():
    search_term = simpledialog.askstring("Search", "Enter name or phone to search:")
    results = search_contact(contacts, search_term)
    if results:
        search_results_window = tk.Toplevel(root)
        search_results_window.title("Search Results")
        search_results_window.config(bg="#F0F8FF")
        for i, contact in enumerate(results):
            tk.Label(search_results_window, text=f"{i + 1}. Name: {contact.name}, Phone: {contact.phone}", bg="#F0F8FF").pack()
    else:
        messagebox.showinfo("No Results", "No contacts found.")

def update_contact_ui():
    search_term = simpledialog.askstring("Search", "Enter name or phone to search:")
    results = search_contact(contacts, search_term)
    if results:
        contact = results[0]
        current_details = f"Current details: Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}"
        messagebox.showinfo("Current Details", current_details)
        
        name = simpledialog.askstring("Input", "Enter new name (leave blank to keep current):")
        phone = simpledialog.askstring("Input", "Enter new phone (leave blank to keep current):")
        email = simpledialog.askstring("Input", "Enter new email (leave blank to keep current):")
        address = simpledialog.askstring("Input", "Enter new address (leave blank to keep current):")
        
        update_contact(contact, name, phone, email, address)
        messagebox.showinfo("Success", "Contact updated successfully.")
    else:
        messagebox.showinfo("No Results", "No contact found.")

def delete_contact_ui():
    search_term = simpledialog.askstring("Search", "Enter name or phone to search:")
    results = search_contact(contacts, search_term)
    if results:
        contact = results[0]
        contact_details = f"Details: Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}"
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete this contact?\n\n{contact_details}")
        if confirm:
            delete_contact(contacts, contact)
            messagebox.showinfo("Success", "Contact deleted successfully.")
    else:
        messagebox.showinfo("No Results", "No contact found.")

root = tk.Tk()
root.title("Contact Book")
root.config(bg="#ADD8E6")

button_bg = "#87CEEB"
button_fg = "#000000"

tk.Button(root, text="Add Contact", command=add_contact_ui, bg=button_bg, fg=button_fg).pack(pady=5)
tk.Button(root, text="View Contacts", command=view_contacts_ui, bg=button_bg, fg=button_fg).pack(pady=5)
tk.Button(root, text="Search Contact", command=search_contact_ui, bg=button_bg, fg=button_fg).pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact_ui, bg=button_bg, fg=button_fg).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact_ui, bg=button_bg, fg=button_fg).pack(pady=5)
tk.Button(root, text="Quit", command=root.quit, bg=button_bg, fg=button_fg).pack(pady=5)

root.mainloop()
