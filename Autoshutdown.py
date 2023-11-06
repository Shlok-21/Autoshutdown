import os
import time
from tkinter import *

# Autoshutdown
def schedule_shutdown(minutes):
    seconds = minutes * 60
    time.sleep(seconds)
    label = Label(text ="time up")
    label.grid(row = 1, column = 1)
    os.system("shutdown /s /t 1")
    

def on_button_click():
    minutes = int(entry1.get())
    schedule_shutdown(minutes)


# GUI
root = Tk()
root.title("AutoShutdown")
root.geometry("330x150")

# Header Label
header_label = Label(text="AutoShutdown", font=("Arial", 20))
header_label.grid(row=0, column=0, columnspan=3, pady=(10, 0))

label1 = Label(text="Enter minutes before shutdown")
entry1 = Entry()
button1 = Button(text="Shutdown", command=on_button_click)

label1.grid(row=1, column=0, padx=10, pady=(20, 5), sticky="e")
entry1.grid(row=1, column=1, pady=(20, 5), sticky="w")
button1.grid(row=2, column=0, columnspan=2, pady=(10, 20))

root.mainloop()
