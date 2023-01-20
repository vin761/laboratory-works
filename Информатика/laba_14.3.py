from tkinter import *

root = Tk()

a = Label(text="Введите элементы последовательности")
A = Entry(width=20)

btn_sred = Button(text="sred")
btn_clear = Button(text="Clear")

Lbl = Label(bg='black', fg='white', width=20)

def sred(event):
    a = A.get()
    a = a.split()
    k = 0
    s = 0
    while int(a[k]) < 0:
        s += int(a[k])
        k += 1
    Lbl['text'] = str(s / k)

def clear(event):
    Lbl['text'] = ''

btn_sred.bind('<Button-1>', sred)
btn_clear.bind('<Button-1>', clear)

a.pack()
A.pack()
btn_sred.pack()
btn_clear.pack()
Lbl.pack()

root.mainloop()