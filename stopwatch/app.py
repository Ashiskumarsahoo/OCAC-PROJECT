import tkinter as tk
import time
from datetime import datetime

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")

        self.running = False
        self.start_time = None
        self.elapsed_time = 0
        self.lap_times = []

        self.time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48), fg="red")
        self.time_label.pack()

        self.date_time_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.date_time_label.pack()

        self.lap_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.lap_label.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side="left")

        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(side="left")

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side="left")

        self.lap_button = tk.Button(root, text="Lap", command=self.lap)
        self.lap_button.pack(side="left")

        self.update_date_time()

    def update_time(self):
        if self.running:
            now = time.time()
            self.elapsed_time = now - self.start_time
            minutes, seconds = divmod(self.elapsed_time, 60)
            hours, minutes = divmod(minutes, 60)
            self.time_label.config(text=f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}")
            self.root.after(1000, self.update_time)

    def update_date_time(self):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.date_time_label.config(text=now)
        self.root.after(1000, self.update_date_time)

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            self.update_time()

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.lap_times.clear()
        self.time_label.config(text="00:00:00")
        self.lap_label.config(text="")

    def lap(self):
        if self.running:
            lap_time = time.time() - self.start_time
            minutes, seconds = divmod(lap_time, 60)
            hours, minutes = divmod(minutes, 60)
            self.lap_times.append(f"Lap {len(self.lap_times) + 1}: {int(hours):02}:{int(minutes):02}:{int(seconds):02}")
            self.lap_label.config(text="\n".join(self.lap_times))

root = tk.Tk()
stopwatch = Stopwatch(root)
root.mainloop()
