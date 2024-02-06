import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(master, width=50)
        self.task_entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=1, column=0, padx=5, pady=5)

        self.update_button = tk.Button(master, text="Update Task", command=self.update_task)
        self.update_button.grid(row=1, column=1, padx=5, pady=5)

        self.task_listbox = tk.Listbox(master, width=50)
        self.task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.track_button = tk.Button(master, text="Track Task", command=self.track_task)
        self.track_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.complete_button = tk.Button(master, text="Complete Task", command=self.complete_task)
        self.complete_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.clear_button = tk.Button(master, text="Clear Completed Tasks", command=self.clear_completed_tasks)
        self.clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            updated_task = self.task_entry.get()
            if updated_task:
                self.tasks[selected_index[0]]["task"] = updated_task
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)

    def track_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_task = self.tasks[selected_index[0]]["task"]
            messagebox.showinfo("Task", selected_task)
        else:
            messagebox.showerror("Error", "Please select a task to track.")

    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks[selected_index[0]]["completed"] = True
            self.update_task_listbox()

    def clear_completed_tasks(self):
        self.tasks = [task for task in self.tasks if not task["completed"]]
        self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_text = "✔️ " + task["task"] if task["completed"] else task["task"]
            self.task_listbox.insert(tk.END, task_text)

def main():
    root = tk.Tk()
    todo_app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
