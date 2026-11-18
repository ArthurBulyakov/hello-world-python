import tkinter as tk
from datetime import datetime

def update_time():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    label.config(text=now)
    root.after(1000, update_time)

root = tk.Tk()
root.title("Current Date and Time")
root.geometry("300x100")

label = tk.Label(root, font=("Arial", 20))
label.pack(expand=True)

update_time()
root.mainloop()
