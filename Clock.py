import tkinter as tk
from tkinter import messagebox
from datetime import datetime

root = tk.Tk()
root.title("Real Time Clock")
root.geometry("480x380")

time_label = tk.Label(root, text="00:00:00", font=("Consolas", 40))
time_label.pack(pady=50)

date_label = tk.Label(root, text="", font=("Segoe UI", 14))
date_label.pack()

alarm_frame = tk.Frame(root)
alarm_frame.pack(pady=10)

alarm_entry = tk.Entry(alarm_frame, font=("Consolas", 14), width=10, justify="center")
alarm_entry.insert(0, "HH:MM AM/PM")
alarm_entry.pack()

alarm_time = None

def set_alarm():
    global alarm_time
    alarm_time = alarm_entry.get()
    messagebox.showinfo("Alarm", f"Alarm diset pada {alarm_time}")

alarm_button = tk.Button(alarm_frame, text="Set Alarm", command=set_alarm)
alarm_button.pack(pady=5)

def update_time():
    now = datetime.now()

    waktu_sekarang = now.strftime("%I:%M:%S %p")
    time_label.config(text=waktu_sekarang)

    tanggal_sekarang = now.strftime("%A, %d %B %Y")
    date_label.config(text=tanggal_sekarang)

    waktu_tanpa_detik = now.strftime("%I:%M %p")
    if alarm_time == waktu_tanpa_detik:
        messagebox.showinfo("Alarm", "Waktunya sudah tiba! ⏰")

    root.after(1000, update_time)

update_time()

root.mainloop()