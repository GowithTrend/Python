import tkinter as tk
from tkinter import messagebox

class MoodMeter:
    def _init_(self, root):
        self.root = root
        self.root.title("Mood Meter")
        self.root.config(bg="#f2f2f2")

        self.mood_label = tk.Label(root, text="How do you feel?", font=("Helvetica", 36, "bold"), bg="#f2f2f2", fg="#4c4c4c")
        self.mood_label.pack(pady=20)

        self.emoji_label = tk.Label(root, text="🙂", font=("Helvetica", 64), bg="#f2f2f2")
        self.emoji_label.pack(pady=20)

        self.button_frame = tk.Frame(root, bg="#f2f2f2")
        self.button_frame.pack()

        self.emotions = [
            {"text": "Happy", "emoji": "😄", "message": "You're doing great! Keep shining!"},
            {"text": "Neutral", "emoji": "😐", "message": "Take a deep breath, stay calm!"},
            {"text": "Sad", "emoji": "😢", "message": "Relax, don't stress! Everything will be fine."},
            {"text": "Angry", "emoji": "😠", "message": "Take a break, go for a walk!"},
            {"text": "Excited", "emoji": "😆", "message": "Yay! Let's celebrate!"},
            {"text": "Fearful", "emoji": "😨", "message": "You're safe! Don't worry."},
        ]

        for emotion in self.emotions:
            tk.Button(self.button_frame, text=emotion["text"], font=("Helvetica", 14), bg="#e6e6e6", fg="#4c4c4c",
                      command=lambda e=emotion: self.set_mood(e["emoji"], e["message"])).pack(side="left", padx=10)

        self.inspiration_label = tk.Label(root, text="", font=("Helvetica", 18, "italic"), bg="#f2f2f2", fg="#4c4c4c")
        self.inspiration_label.pack(pady=20)

        self.update_inspiration()

    def set_mood(self, mood, message):
        self.emoji_label.config(text=mood)
        messagebox.showinfo("Mood Alert", message)

    def update_inspiration(self):
        inspirations = [
            "Believe in yourself!",
            "You are stronger than you think!",
            "Every day is a new chance!",
            "Smile, it's contagious!",
            "Keep going, don't give up!",
        ]
        self.inspiration_label.config(text=random.choice(inspirations))
        self.root.after(5000, self.update_inspiration)


import random
if _name_ == "_main_":
    root = tk.Tk()
    app = MoodMeter(root)
    root.mainloop()
