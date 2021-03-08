# File: hello2.py
from tkinter import *


def say_hi():
    print("hi there, everyone!")


class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.button = Button(frame,  # master widget
                             text="QUIT",
                             fg="red",
                             command=frame.quit
                             )
        self.button.pack(side=LEFT)
        self.hi_there = Button(frame,
                               text="Hello",
                               command=say_hi
                               )
        self.hi_there.pack(side=LEFT)


# top = tkinter.Tk()
# # 进入消息循环
# top.mainloop()
root = Tk()
# listB = Listbox(root)
# listB.insert(0, 1)
# listB.insert(0, 2)
# listB.pack()
app = App(root)
root.mainloop()
