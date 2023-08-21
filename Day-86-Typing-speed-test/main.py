import time
import tkinter as tk
from tkinter import messagebox

class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.text_to_type = "The quick brown fox jumps over the lazy dog."
        self.current_input = ""
        self.start_time = None

        self.text_label = tk.Label(self.root, text=self.text_to_type)
        self.text_label.pack()

        self.input_entry = tk.Entry(self.root)
        self.input_entry.pack()

        self.start_button = tk.Button(self.root, text="Start Typing Test", command=self.start_typing)
        self.start_button.pack()

    def start_typing(self):
        self.start_time = time.time()
        self.start_button.config(state=tk.DISABLED)
        self.input_entry.bind("<KeyRelease>", self.check_typing)

    def check_typing(self, event):
        self.current_input = self.input_entry.get()
        if self.current_input == self.text_to_type:
            self.calculate_typing_speed()
        elif len(self.current_input) >= len(self.text_to_type):
            self.show_result("Typed text doesn't match.")

    def calculate_typing_speed(self):
        end_time = time.time()
        typing_time = end_time - self.start_time
        words_typed = len(self.text_to_type.split())
        typing_speed = int(words_typed / typing_time * 60)
        self.show_result(f"Your typing speed: {typing_speed} words per minute.")

    def show_result(self, message):
        messagebox.showinfo("Typing Speed Test Result", message)
        self.input_entry.delete(0, tk.END)
        self.start_button.config(state=tk.NORMAL)
        self.input_entry.unbind("<KeyRelease>")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()
