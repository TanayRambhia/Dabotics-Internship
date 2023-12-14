import tkinter as tk
from datetime import datetime
import winsound  # for playing the alarm sound on Windows

def set_alarm():
    alarm_time = entry.get()
    try:
        alarm_hour, alarm_minute = map(int, alarm_time.split(':'))
        if alarm_hour < 0 or alarm_hour > 12 or alarm_minute < 0 or alarm_minute > 59:
            raise ValueError("Invalid time format")
        
        now = datetime.now()
        if alarm_hour <= 12:  # Convert to 24-hour format
            if alarm_hour == 12:
                alarm_hour = 0
            alarm_hour += now.hour % 12
        else:
            alarm_hour += 12
        
        alarm = now.replace(hour=alarm_hour, minute=alarm_minute, second=0, microsecond=0)
        
        if alarm <= now:
            alarm = alarm.replace(day=alarm.day + 1)

        time_difference = alarm - now
        time_to_wait = time_difference.total_seconds()
        
        def sound_alarm():
            root.title("Alarm Ringing!")
            winsound.Beep(1000, 1000)  # Beep sound for 1 second (change as needed)
            snooze_button.pack()

        def snooze_alarm():
            snooze_button.pack_forget()
            root.title("Python Alarm Clock")
            root.after(300 * 1000, sound_alarm)  # Snooze for 5 minutes (300 seconds)
        
        root.after(int(time_to_wait * 1000), sound_alarm)
        status_label.config(text=f"Alarm set for {alarm_time}")
        alarms.append(alarm_time)
        alarms_listbox.insert(tk.END, alarm_time)
    except ValueError:
        status_label.config(text="Invalid input format. Use HH:MM")

root = tk.Tk()
root.title("Python Alarm Clock")

frame = tk.Frame(root, bg="#f0f0f0")  # Setting a background color
frame.pack(padx=20, pady=20)

label = tk.Label(frame, text="Enter alarm time (HH:MM):", bg="#f0f0f0", font=("Arial", 12))
label.pack()

entry = tk.Entry(frame, font=("Arial", 12))
entry.pack()

set_button = tk.Button(frame, text="Set Alarm", command=set_alarm, font=("Arial", 12), bg="#55aacc", fg="white")
set_button.pack()

status_label = tk.Label(frame, text="", font=("Arial", 12), bg="#f0f0f0")
status_label.pack()

alarms = []  # Store alarm times

def sound_alarm():
    root.title("Alarm Ringing!")
    winsound.Beep(1000, 1000)  # Beep sound for 1 second (change as needed)
    snooze_button.pack()

def snooze_alarm():
    snooze_button.pack_forget()
    root.title("Python Alarm Clock")
    root.after(300 * 1000, sound_alarm)  # Snooze for 5 minutes (300 seconds)

snooze_button = tk.Button(frame, text="Snooze", command=snooze_alarm, font=("Arial", 12), bg="#55aacc", fg="white")

alarms_frame = tk.Frame(root, bg="#f0f0f0")
alarms_frame.pack(padx=20, pady=10)
alarms_label = tk.Label(alarms_frame, text="Alarms:", font=("Arial", 12), bg="#f0f0f0")
alarms_label.pack()
alarms_listbox = tk.Listbox(alarms_frame, font=("Arial", 12))
alarms_listbox.pack()

root.mainloop()
