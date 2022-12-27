import tkinter as tk

class TaskManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Task Manager")
        self.geometry("400x300")

        self.task_frame = tk.Frame(self)
        self.task_frame.pack(side="top", fill="x")
        self.task_list = tk.Listbox(self.task_frame, width=50)
        self.task_list.pack(side="left")
#
        self.scrollbar = tk.Scrollbar(self.task_frame)
        self.scrollbar.pack(side="right", fill="y")
        self.task_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_list.yview)

        self.add_task_frame = tk.Frame(self)
        self.add_task_frame.pack(side="bottom", fill="x")
        self.add_task_label = tk.Label(self.add_task_frame, text="Add new task:")
        self.add_task_label.pack(side="left")
        self.add_task_entry = tk.Entry(self.add_task_frame, width=50)
        self.add_task_entry.pack(side="left")
        self.add_task_button = tk.Button(self.add_task_frame, text="Add", command=self.add_task)
        self.add_task_button.pack(side="left")
        self.delete_task_button = tk.Button(self.add_task_frame, text="Delete", command=self.delete_task)
        self.delete_task_button.pack(side="left")

    def add_task(self):
        task = self.add_task_entry.get()
        self.task_list.insert("end", task)
        self.add_task_entry.delete(0, "end")

    def delete_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            self.task_list.delete(selected_task)
        else:
            tk.messagebox.showwarning("Warning", "No task selected!")


if __name__ == "__main__":
    app = TaskManager()
    app.mainloop()
