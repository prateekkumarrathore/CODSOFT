import tkinter as tk
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            result_label.config(text="Invalid length. Please enter a positive integer.")
            return
        password = generate_password(length)
        result_label.config(text="Generated password: " + password)
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid integer.")

# Create tkinter window
window = tk.Tk()
window.title("Password Generator")

# Create widgets
length_label = tk.Label(window, text="Enter password length:")
length_label.pack()

length_entry = tk.Entry(window)
length_entry.pack()

generate_button = tk.Button(window, text="Generate Password", command=generate_and_display_password)
generate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Run the tkinter event loop
window.mainloop()
