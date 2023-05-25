import tkinter as tk
import random
pw=50
ph=50
countweight=random.randrange(4,7)
countheight=random.randrange(3,10)
win=tk.Tk()
canvas=tk.Canvas(width=300,height=450,bg="grey")
img=tk.PhotoImage(file="image/ostrov3.png")
img1=tk.PhotoImage(file="image/ostrov0.png")
canvas.pack()
for y in range(countheight):
    for x in range(countheight):
        result=random.random()
        if result<=0.2:
            #img=tk.PhotoImage(file="image/ostrov3.png")
            canvas.create_image(pw*x,ph*y,anchor="nw",image=img)
        else:
            #img=tk.PhotoImage(file="image/ostrov0.png")
            canvas.create_image(pw * x, ph * y, anchor="nw", image=img1)
win.mainloop()