import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("Real Time Clock")
root.geometry("480x260")

time_label = tk.Label(root, text="00:00:00", font=("Consolas", 40))
time_label.pack(pady=50)

def update_time():
    waktu_sekarang = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=waktu_sekarang)
    root.after(1000, update_time)

update_time()

root.mainloop()