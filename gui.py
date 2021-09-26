import pyspeedtest
from tkinter import *


def Speed_test():
    speedTest = pyspeedtest.SpeedTest(textArea.get())
    myping.set(speedTest.ping())
    down.set(speedTest.download())



master = Tk()
myping = StringVar()
down = StringVar()

Label(master, text="Enter Website URL to ping").grid(row=0, sticky=W)
Label(master, text="Ping test result in ms:").grid(row=3, sticky=W)
Label(master, text="Download test result in bps:").grid(row=4, sticky=W)

pingResult = Label(master, text="", textvariable=myping, ).grid(row=3, column=1, sticky=W)
downloadResult = Label(master, text="", textvariable=down, ).grid(row=4, column=1, sticky=W)
textArea = Entry(master)

textArea.grid(row=0, column=1)

b = Button(master, text="Check", command=Speed_test)
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

mainloop()