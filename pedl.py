import tkinter as tk
import random
win = tk.Tk()
w = 600
h = 600
canvas = tk.Canvas(win, height = h, width = w, bg = "white")
canvas.pack()
a=0
b=0
c=0
d=0
direction=2

game=True
while game==True:
    while  a!=0 or a!=600 or b!=0 or b!=600 or c!=0 or c!=600 or d!=0 or d!=600:
        canvas.delete("all")
        canvas.after(100,canvas.create_oval(a, b, c, d))
        if direction==1:
            a+=1
            b+=1
        if direction == 2:
            b += 1
            c += 1
        if direction==3:
            c+=1
            d+=1
        if direction == 4:
            d += 1
            a += 1
        def stopka():
            global stopped
            stopped=True
            a=0
    if stopped==True:
        break
    direction=random.randrange(0,4)

button1 = tk.Button(win, text= "stop",command = stopka)
button1.pack()
win.mainloop()