from tkinter import *

root = Tk()

a = Label(text="Введите A")
A = Entry(width=20)
b = Label(text="Введите B")
B = Entry(width=20)
c = Label(text="Введите C")
C = Entry(width=20)

btn_square = Button(text="Площадь")
btn_volume = Button(text="Объём")
btn_clear = Button(text="Clear")

Lbl = Label(bg='black', fg='white', width=20)

def square(event):
    a = int(A.get())
    b = int(B.get())
    c = int(C.get())
    Lbl['text'] = str(2*(a * b + b * c + a * c))

def volume(event):
    a = int(A.get())
    b = int(B.get())
    c = int(C.get())
    Lbl['text'] = str(a * b * c)

def clear(event):
    Lbl['text'] = ''

btn_square.bind('<Button-1>', square)
btn_volume.bind('<Button-1>', volume)
btn_clear.bind('<Button-1>', clear)
flag = Checkbutton()
Button = Radiobutton(root, text = 'aaaaa', value = 1)

flag.pack()
Button.pack()
a.pack()
A.pack()
b.pack()
B.pack()
c.pack()
C.pack()
btn_square.pack()
btn_volume.pack()
btn_clear.pack()
Lbl.pack()

root.mainloop()