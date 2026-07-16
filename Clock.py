import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import winsound

root = tk.Tk()
root.title("Real Time Clock")
root.geometry("480x380")
BG_COLOR = "#121212"
CARD_COLOR = "#1e1e1e"
ACCENT_COLOR = "#00e5ff"
TEXT_COLOR = "#e0e0e0"
MUTED_COLOR = "#888888"

root.configure(bg=BG_COLOR)

time_label = tk.Label(root, text="00:00:00", font=("Consolas", 48, "bold"), bg=BG_COLOR, fg=ACCENT_COLOR)
time_label.pack(pady=50)

date_label = tk.Label(root, text="", font=("Segoe UI", 13), bg=BG_COLOR, fg=MUTED_COLOR)
date_label.pack()

alarm_frame = tk.Frame(root, bg=BG_COLOR)
alarm_frame.pack(pady=10)

alarm_entry = tk.Entry(alarm_frame, font=("Consolas", 14), width=12, justify="center", bg=CARD_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR, relief="flat", bd=8)
alarm_entry.insert(0, "HH:MM AM/PM")
alarm_entry.pack()

alarm_time = None

def set_alarm():
    global alarm_time
    input_user = alarm_entry.get().strip()

    try:
        datetime.strptime(input_user, "%I:%M %p")
        alarm_time = input_user
        messagebox.showinfo("Alarm", f"Alarm diset pada {alarm_time}")
    except ValueError:
        messagebox.showerror("Format Salah", "Format harus HH:MM AM/PM\nContoh: 03:09 PM")

def cancel_alarm():
    global alarm_time
    alarm_time = None
    messagebox.showinfo("Alarm", "Alarm dibatalkan")

alarm_button = tk.Button(alarm_frame, text="Set Alarm", command=set_alarm, bg=ACCENT_COLOR, fg="#000000", font=("Segoe UI", 10, "bold"), relief="flat", padx=15, pady=6, cursor="hand2", activebackground="#00b8cc")
alarm_button.pack(pady=5)

cancel_button = tk.Button(alarm_frame, text="Cancel Alarm", command=cancel_alarm, bg=CARD_COLOR, fg=TEXT_COLOR, font=("Segoe UI", 10), relief="flat", padx=15, pady=6, cursor="hand2", activebackground="#333333")
cancel_button.pack(pady=5)

def update_time():
    global alarm_time
    now = datetime.now()

    waktu_sekarang = now.strftime("%I:%M:%S %p")
    time_label.config(text=waktu_sekarang)

    tanggal_sekarang = now.strftime("%A, %d %B %Y")
    date_label.config(text=tanggal_sekarang)

    waktu_tanpa_detik = now.strftime("%I:%M %p")
    if alarm_time == waktu_tanpa_detik:
        winsound.Beep(1000, 500)
        winsound.Beep(1000, 500)
        winsound.Beep(1000, 500)
        messagebox.showinfo("Alarm", "Waktunya sudah tiba! ⏰")
        alarm_time = None    

    root.after(1000, update_time)

update_time()

root.mainloop()