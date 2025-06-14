import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Custom Styled Form")
root.geometry("350x300")
root.configure(bg="black")

style = ttk.Style()
style.theme_use("winnative")

# Label Style
style.configure("Custom.TLabel", foreground="white", background="black", font=("Arial", 12))

# Entry Style
style.configure("Custom.TEntry", foreground="blue", padding=5)

# Button Style with map
style.configure("Custom.TButton",
                font=("Arial", 11, "bold"),
                background="#0066cc",
                foreground="white",
                padding=8)

style.map("Custom.TButton",
          background=[("active", "#004080"), ("pressed", "#00264d")],
          foreground=[("active", "yellow")])

# Widgets
ttk.Label(root, text="Name:", style="Custom.TLabel").pack(pady=5)
entry = ttk.Entry(root, style="Custom.TEntry")
entry.pack(pady=5)

ttk.Label(root, text="Email:", style="Custom.TLabel").pack(pady=5)
entry2 = ttk.Entry(root, style="Custom.TEntry")
entry2.pack(pady=5)

ttk.Button(root, text="Submit", style="Custom.TButton").pack(pady=20)

root.mainloop()
