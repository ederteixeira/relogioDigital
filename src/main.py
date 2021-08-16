from tkinter import *
from tkinter import ttk
from tkinter import font

import datetime


def fechar(*args):
    estrutura.destroy()


def clock_time():
    time = datetime.datetime.now()
    time = (time.strftime("%H:%M:%S"))
    texto.set(time)
    estrutura.after(1000, clock_time)


estrutura = Tk()
estrutura.title("Relogio digital")
estrutura.attributes("-fullscreen", False)
estrutura.geometry('400x150')
estrutura.resizable(width=0, height=0)

estrutura.configure(background='black')
estrutura.bind("x", fechar)
estrutura.after(1000, clock_time)

fonte = font.Font(family="Helvetica", size=60, weight='bold')
texto = StringVar()
lbl = ttk.Label(estrutura, textvariable=texto, font=fonte, foreground="white", background="black")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

estrutura.mainloop()
