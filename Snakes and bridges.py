import tkinter as tk
import random
pw=50
ph=50
countwidth=random.randrange(4,7)
countheight=random.randrange(3,10)
win=tk.Tk()
canvas=tk.Canvas(width=countwidth*pw+100,height=countheight*ph,bg="grey")
canvas.pack()
water=[]
islands=[]
img=tk.PhotoImage(file="ostrov3.png")
img1=tk.PhotoImage(file="ostrov0.png")
img2=tk.PhotoImage(file="ostrov1.png")
img3=tk.PhotoImage(file="ostrov2.png")
img4=tk.PhotoImage(file="ostrov_kruh0.png")
img4=tk.PhotoImage(file="ostrov_kruh1.png")

def zmenar(e):
    print("I klikd.")
    zoz=canvas.find_overlapping(e.x,e.x,e.x+1,e.y+1)
    if len(zoz)!=0 and zoz[0] in water:
        print("You klikd on vodu.")
        nx=(e.x//pw)*pw
        ny=(e.y//ph)*ph
        temp=zoz[0]
        canvas.delete(temp)
        water.remove(temp)

        canvas.create_image(nx,ny,anchor="nw",image=img2,tag="most")

def otáčač(e):
    zoz = canvas.find_overlapping(e.x, e.x, e.x + 1, e.y + 1)
    print(canvas.itemcget(zoz[0],"image"))
    if canvas.itemconfig(zoz[0],image=img3):
        canvas.itemconfig(zoz[0],image=img3)

def setup():
    global water,islands,counterwidth
    for y in range(countheight):
        for x in range(countheight):
            result=random.random()
            if result<=0.2:
                #img=tk.PhotoImage(file="image/ostrov3.png")
                water.append(canvas.create_image(pw*x,ph*y,anchor="nw",image=img))
            else:
                #img=tk.PhotoImage(file="image/ostrov0.png")
                islands.append(canvas.create_image(pw * x, ph * y, anchor="nw", image=img1))
    canvas.create_image(counterwidth*pw+50,0,anchor="nw",image=img4,tags="zmenar")

canvas.bind("<Button-1>",zmenar)
canvas.tag_bind("most","<Button-1>",otáčač)
setup()
win.mainloop()