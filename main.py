# This is a sample Python script.
# - AI-MINOR-AUGUST
# Count-Down Timer

# importing the modules
from tkinter import *
import time
from tkinter import StringVar, Tk

running: bool = False

# Frame Creation
root: Tk = Tk()
root.title("Count-Down Timer")
root.geometry("400x400")
root.config(bg="gray")
root.resizable(False, False)

# Main Heading
Title_Name = Label(root, text="Count-Down Timer", font="Times 30 bold", fg="white", bg="grey")
Title_Name.pack(pady=10)


def Current_time():
    ctime = time.strftime('%H:%M:%S %p')
    current_time.config(text=ctime)
    current_time.after(1000, Current_time)


current_time = Label(root, font=("arial", 15, "bold"), text="", fg="black", bg="white")
current_time.place(x=170, y=70)
Current_time()

# Hour INPUT Code
hour: StringVar = StringVar()
Entry(root, textvariable=hour, width=2, font="arial 35", bg="grey", bd=0).place(x=60, y=130)
hour.set("00")
Label(root, text="hours", bd=0, font="arial 12", bg="grey").place(x=115, y=160)

# Minute INPUT Code
minute: StringVar = StringVar()
Entry(root, textvariable=minute, width=2, font="arial 35", bg="grey", bd=0).place(x=170, y=130)
minute.set("00")
Label(root, text="min", bd=0, font="arial 12", bg="grey").place(x=225, y=160)

# Seconds INPUT Code
seconds: StringVar = StringVar()
Entry(root, textvariable=seconds, width=2, font="arial 35", bg="grey", bd=0).place(x=280, y=130)
seconds.set("00")
Label(root, text="sec", bd=0, font="arial 12", bg="grey").place(x=340, y=160)


# Timer Code
def Timer():
    times: int = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(seconds.get())

    while times > -1:
        mins: int
        mins, sec = (times // 60, times % 60)
        hrs = 0
        if mins > 60:
            hrs, mins = (mins // 60, mins % 60)
        seconds.set(str(sec))
        minute.set(str(mins))
        hour.set(str(hrs))

        root.update()
        time.sleep(1)

        times -= 1


def Start():
    global running
    if not running:
        Timer()
        running = TRUE


def Reset():
    hour.set(str("00"))
    minute.set(str("00"))
    seconds.set(str("00"))
    root.update()
    time.sleep(1000)


def Cancel():
    root.destroy()


def Pause():
    global running
    if running:
        hour.after_cancel(root.update())
        minute.after_cancel(root.update())
        seconds.after_cancel(root.update())
        running = False


# Start Button
Start_button = Button(root, text="Start", bg="#008080", bd=0, fg="#fff", width=20, height=2, font="times 12 bold",
                      command=Start)
Start_button.pack(padx=15, pady=14)
Start_button.place(x=124, y=200)

# Reset Button
Reset_button = Button(root, text="Reset", bg="#008080", bd=0, fg="#fff", width=20, height=2, font="times 12 bold",
                      command=Reset)
Reset_button.pack(padx=15, pady=14)
Reset_button.place(x=124, y=250)

# Pause Button
Pause_button = Button(root, text="Pause", bg="#008080", bd=0, fg="#fff", width=20, height=2, font="times 12 bold",
                      )
Pause_button.pack(padx=15, pady=14)
Pause_button.place(x=124, y=300)

# Cancel Button
Cancel_button = Button(root, text="Cancel", bg="#008080", bd=0, fg="#fff", width=20, height=2, font="times 12 bold",
                       command=Cancel)
Cancel_button.pack(padx=15, pady=14)
Cancel_button.place(x=124, y=350)

root.mainloop()
