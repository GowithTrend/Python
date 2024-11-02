import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
label = tk.Label(root, font=("Helvetica", 48), background="black", foreground="cyan")
label.pack(anchor="center")
def time():
    current_time = strftime("%H:%M:%S %p")
    label.config(text=current_time)
    label.after(1000, time)

time()
root.mainloop()
