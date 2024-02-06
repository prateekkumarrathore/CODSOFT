import tkinter as tk

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation_choice = operation_var.get()

        if operation_choice == 1:
            result = add(num1, num2)
        elif operation_choice == 2:
            result = subtract(num1, num2)
        elif operation_choice == 3:
            result = multiply(num1, num2)
        elif operation_choice == 4:
            result = divide(num1, num2)
        else:
            result = "Invalid operation choice."

        result_label.config(text=f"Result: {result}")

    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")

root = tk.Tk()
root.title("Simple Calculator")

# Entry widgets for numbers
entry_num1 = tk.Entry(root, width=10)
entry_num1.grid(row=0, column=0, padx=5, pady=5)

entry_num2 = tk.Entry(root, width=10)
entry_num2.grid(row=0, column=1, padx=5, pady=5)

# Radio buttons for operations
operation_var = tk.IntVar()
addition_radio = tk.Radiobutton(root, text="+", variable=operation_var, value=1)
addition_radio.grid(row=1, column=0, padx=5, pady=5)

subtraction_radio = tk.Radiobutton(root, text="-", variable=operation_var, value=2)
subtraction_radio.grid(row=1, column=1, padx=5, pady=5)

multiplication_radio = tk.Radiobutton(root, text="*", variable=operation_var, value=3)
multiplication_radio.grid(row=1, column=2, padx=5, pady=5)

division_radio = tk.Radiobutton(root, text="/", variable=operation_var, value=4)
division_radio.grid(row=1, column=3, padx=5, pady=5)

# Button to perform calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=2, column=0, columnspan=4, pady=10)

# Label to display result
result_label = tk.Label(root, text="Result: ", font=("Helvetica", 12))
result_label.grid(row=3, column=0, columnspan=4, pady=10)

root.mainloop()
