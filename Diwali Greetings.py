import tkinter as tk
from tkinter import font
import time
import threading
import winsound  # Works on Windows for simple sound effects

# Function to animate lamps and show greeting
def show_greeting():
    greeting_text = "Happy Diwali to Everyone! 🎉🪔"
    animated_text = ""
    for char in greeting_text:
        animated_text += char
        wish_label.config(text=animated_text)
        root.update()
        time.sleep(0.05)  # Delay for animation effect

# Function to play a Diwali sound (simple beep effect)
def play_sound():
    # Beep sound effect (Windows).
    for _ in range(3):
        winsound.Beep(1000, 150)  # Frequency and duration of each beep
        time.sleep(0.2)

# Run sound and greeting animation in parallel
def start_greeting():
    threading.Thread(target=show_greeting).start()
    threading.Thread(target=play_sound).start()

# Set up main window
root = tk.Tk()
root.title("Diwali Wishes")
root.geometry("400x300")
root.configure(bg="#ffebcc")

# Custom font styles
title_font = font.Font(family="Helvetica", size=18, weight="bold")
wish_font = font.Font(family="Arial", size=14, weight="bold")

# Title Label
title_label = tk.Label(root, text="🎆 Diwali Greetings 🎆", font=title_font, bg="#ffebcc", fg="#d97706")
title_label.pack(pady=20)

# Wish Label (animated)
wish_label = tk.Label(root, text="", font=wish_font, bg="#ffebcc", fg="#d97706")
wish_label.pack(pady=10)

# Button to trigger greeting and sound
wish_button = tk.Button(root, text="Send Diwali Wishes", command=start_greeting, font=("Arial", 12), bg="#ff6600", fg="white", borderwidth=0, highlightthickness=0)
wish_button.pack(pady=20)

# Animated Diya (lamp) emojis under the greeting
diya_label = tk.Label(root, text="🪔 " * 10, font=("Arial", 20), bg="#ffebcc", fg="#ff6600")
diya_label.pack(pady=20)

root.mainloop()
