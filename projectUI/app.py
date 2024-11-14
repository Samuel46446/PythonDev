from doctest import master
from tkinter import  *
from tkinter import Label

def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

def confirm(result):
    result = result + 1

def increase():
    value = int(popUp["text"])
    popUp["text"] = f"{value + 1}"


window = Tk()

window.title("Mon jeu")
window.geometry("1080x720")
window.minsize(480,480)

saisie = Entry()
name = saisie.get()
result = 0#int(name, 2)
valider = Button(master=window, text="Click me!",width=25,height=5,bg="blue",fg="yellow", command=increase)
popUp=Label(text=str(result))
frame = Frame(master=window, width=50, height=50, bg="red")
frame.pack(fill=BOTH, side=LEFT, expand=True)
popUp.pack()
valider.pack()
saisie.pack()
lb = Label(text="Main")
lb.pack()
window.mainloop()