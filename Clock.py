import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("Real Time Clock")
root.geometry("480x260")

time_label = tk.Label(root, text="00:00:00", font=("Consolas", 40))
time_label.pack(pady=50)

date_label = tk.Label(root, text="", font=("Segoe UI", 14))
date_label.pack()

def update_time():
    now = datetime.now()

    waktu_sekarang = now.strftime("%H:%M:%S")
    time_label.config(text=waktu_sekarang)

    tanggal_sekarang = now.strftime("%A, %d %B %Y")
    date_label.config(text=tanggal_sekarang)

    root.after(1000, update_time)

update_time()

root.mainloop()