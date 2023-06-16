#### Imports ####
import tkinter as tk
from tkinter import *
import subprocess
import ast
import os

#### Initialize tkinter
root = Tk()
root.title("About")
root.geometry("+300+150")
mainWindow = Frame(root)
mainWindow.grid()

def new_func():
    return """MIt License LeJHuBo
  Copyright (c) 2023 scriptik."""

LICENCE = new_func()

def BtnClose():
    root.quit()

l = Label(mainWindow, text="Developed by: Leonardo\nhttps://github.com/lejhubo\: {}\n".format(LICENCE))
l.grid(row="0", column="0", sticky=E+W+N+S)

btnClose = Button(mainWindow, command=BtnClose, text="Close")
btnClose.grid(row="1", column="0", sticky=E+W+N+S)

root.mainloop()
