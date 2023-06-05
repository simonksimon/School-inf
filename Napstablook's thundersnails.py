import tkinter as tk, random
from tkinter import Canvas
root=tk.Tk()
canvas: Canvas = tk.Canvas(width=700, height=650)
canvas.pack()

a=20
b=30
safety=0

def lodicka(x, y):
    plachta = random.randint(-3, 3)
    canvas.create_line(x, y, x, y-25, x+10+plachta, y-10, x, y-5)
    canvas.create_polygon(x-20, y, x+20, y, x+10, y+8, x-10, y+8)

def start(e):
    global a,b,safety
    c=0
    y="0"
    for i in range(15):
        globals()["var_" + str(i)] = a
    while c<650:
        safety+=1
        if safety==1000:
            print("Safety overheated.")
            break
        b = 30
        canvas.delete("all")
        canvas.create_line(650, 0, 650, 650, fill="red")
        for i in range(15):
            canvas.update()
            globals()["var_" + str(i)]+=random.randint(1,10)
            c = globals()["var_" + str(i)]
            print(str(i+1)+". "+str(c),b)
            b += 35
            lodicka(c, b)
            canvas.update()
            #canvas.after(1)
            if c==650 or c>650:
                y=str(i+1)
                break
    canvas.delete("all")
    canvas.create_line(650, 0, 650, 650, fill="red")
    lodicka(c, b)
    canvas.create_text(350, 325, fill="darkblue", font="Times 15",text=y+" won.")

for i in range(15):
    lodicka(a,b+35)
    b+=35
canvas.create_line(650,0,650,650,fill="red")

canvas.bind("<Button-1>",start)
root.mainloop()