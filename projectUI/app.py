from doctest import master
from tkinter import  *
from tkinter import Label

from vboxapi import xrange


def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

def confirm(result):
    result = result + 1

def increase():
    value = int(popUp["text"])
    popUp["text"] = f"{value + 1}"

class Carre:
    def __init__(self, x : int, y : int, w : int, h : int, color : str):
        self.frame = Frame(master=window, width=w, height=h, bg=color)
        self.frame.pack(fill=BOTH, side=LEFT, expand=True)
        self.frame.place(x=x, y=y)

class Tetriminos:
    def __init__(self, form):
        self.tab = form

    def getRender(self):
        return self.tab

IBarre=Tetriminos([
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1],])

def setRender():
    baseX=120
    baseY=100
    for i in range(4):
        for k in range(4):
            if IBarre.getRender()[i][k] == 1:
                c=Carre(baseX+k*20, baseY+i*20, 20, 20, "red")

window = Tk()

window.title("Mon jeu")
window.geometry("300x400")
window.minsize(300,400)
window.resizable(300,400)

#saisie = Entry()
#name = saisie.get()
#result = 0#int(name, 2)
#valider = Button(master=window, text="Click me!",width=25,height=5,bg="blue",fg="yellow", command=increase)
#popUp=Label(text=str(result))
#frame = Frame(master=window, width=50, height=50, bg="red")
#frame.pack(fill=BOTH, side=LEFT, expand=True)
#popUp.pack()
#valider.pack()
#saisie.pack()

setRender()

#lb = Label(text="Main")
#lb.pack()
window.mainloop()