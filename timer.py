import tkinter as tk
from tkinter import messagebox
import time
import threading

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Timer")

        self.root.geometry("300x300")  # Set the initial window size

        self.time_label = tk.Label(root, text="Set Timer (seconds):", font=("Helvetica", 14))
        self.time_label.pack(pady=10)

        self.time_entry = tk.Entry(root, font=("Helvetica", 14))
        self.time_entry.pack()

        self.start_button = tk.Button(root, text="Start Timer", command=self.start_timer, font=("Helvetica", 14))
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop Timer", command=self.stop_timer, font=("Helvetica", 14))
        self.stop_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Reset Timer", command=self.reset_timer, font=("Helvetica", 14))
        self.reset_button.pack(pady=5)

        self.timer_label = tk.Label(root, text="", font=("Helvetica", 24))
        self.timer_label.pack()

        self.running = False
        self.stopped = False

    def start_timer(self):
        if not self.running:
            try:
                self.remaining_time = int(self.time_entry.get())
                self.update_timer_label()
                self.running = True
                self.stopped = False
                self.timer_thread = threading.Thread(target=self.run_timer)
                self.timer_thread.start()
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

    def stop_timer(self):
        if self.running:
            self.running = False
            self.stopped = True

    def reset_timer(self):
        self.running = False
        self.stopped = False
        self.timer_label.config(text="")
        self.time_entry.delete(0, tk.END)

    def run_timer(self):
        while self.remaining_time > 0 and not self.stopped:
            time.sleep(1)
            self.remaining_time -= 1
            self.update_timer_label()

        if not self.stopped:
            self.timer_label.config(text="Time's up!")
            self.running = False

    def update_timer_label(self):
        self.timer_label.config(text=f"Time left: {self.remaining_time} seconds")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
