from tkinter import *

root = Tk()

a = Label(text="Введите A")
A = Entry(width=30)
b = Label(text="Введите B")
B = Entry(width=30)
c = Label(text="Введите C")
C = Entry(width=30)

btn_check = Button(text="check")
btn_clear = Button(text="Clear")

Lbl = Label(bg='black', fg='white', width=30)

def check(event):
    a = int(A.get())
    b = int(B.get())
    c = int(C.get())
    if a==b==c:
        Lbl['text'] = "Треугольник равносторонний"
    else:
        Lbl['text'] = "Треугольник неравносторонний"

def clear(event):
    Lbl['text'] = ''


btn_check.bind('<Button-1>', check)
btn_clear.bind('<Button-1>', clear)

a.pack()
A.pack()
b.pack()
B.pack()
c.pack()
C.pack()
btn_check.pack()
btn_clear.pack()
Lbl.pack()

root.mainloop()