import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Manager")

        self.contacts = []

        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, sticky="w")
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1)

        self.phone_label = tk.Label(master, text="Phone Number:")
        self.phone_label.grid(row=1, column=0, sticky="w")
        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=1, column=1)

        self.email_label = tk.Label(master, text="Email:")
        self.email_label.grid(row=2, column=0, sticky="w")
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=2, column=1)

        self.address_label = tk.Label(master, text="Address:")
        self.address_label.grid(row=3, column=0, sticky="w")
        self.address_entry = tk.Entry(master)
        self.address_entry.grid(row=3, column=1)

        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(master, text="View Contact List", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.search_label = tk.Label(master, text="Search:")
        self.search_label.grid(row=6, column=0, sticky="w")
        self.search_entry = tk.Entry(master)
        self.search_entry.grid(row=6, column=1)

        self.search_button = tk.Button(master, text="Search", command=self.search_contact)
        self.search_button.grid(row=7, column=0, columnspan=2, pady=5)

        self.contact_listbox = tk.Listbox(master, width=50)
        self.contact_listbox.grid(row=8, column=0, columnspan=2, pady=5)

        self.update_button = tk.Button(master, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=9, column=0, columnspan=2, pady=5)

        self.delete_button = tk.Button(master, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=10, column=0, columnspan=2, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone_number:
            contact = Contact(name, phone_number, email, address)
            self.contacts.append(contact)
            self.clear_entries()
            messagebox.showinfo("Success", "Contact added successfully.")
        else:
            messagebox.showerror("Error", "Name and Phone Number are required fields.")

    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact.name} - {contact.phone_number}")

    def search_contact(self):
        query = self.search_entry.get()
        if query:
            found_contacts = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone_number]
            self.contact_listbox.delete(0, tk.END)
            for contact in found_contacts:
                self.contact_listbox.insert(tk.END, f"{contact.name} - {contact.phone_number}")
        else:
            messagebox.showerror("Error", "Please enter a search query.")

    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            selected_contact = self.contacts[selected_index[0]]
            self.name_entry.insert(0, selected_contact.name)
            self.phone_entry.insert(0, selected_contact.phone_number)
            self.email_entry.insert(0, selected_contact.email)
            self.address_entry.insert(0, selected_contact.address)
            self.contacts.pop(selected_index[0])
            self.contact_listbox.delete(selected_index)

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            self.contacts.pop(selected_index[0])
            self.contact_listbox.delete(selected_index)

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
