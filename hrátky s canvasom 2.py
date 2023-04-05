import tkinter as tk
win=tk.Tk()

width=500
height=500
x=0
y=0

def klikacka(e):
    #print("Has happened.")
      #If I clicked on our object, remember the coordinates
    #print(canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1))
    global x,y
    zoz=canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if ob1 in zoz:
        x=e.x
        y=e.y

def pohybovac(e):
    global x, y
    print("Am clicked and dragged (and dropped)")
    if x!=0 and y!=0:
        dx=e.x-x
        dy=e.y-y
        canvas.move(ob1,dx,dy)
        x=e.x
        y=e.y

def pustac(e):
    global x,y
    x,y=0,0

canvas=tk.Canvas(win,height=height, width=width,bg="white")
canvas.pack()

ob1=canvas.create_polygon(10,10,50,80,140,82,fill="blue")
canvas.bind("<Button-1>",klikacka)
canvas.bind("<B1-Motion>",pohybovac)
canvas.bind("<ButtonRelease-1>",pustac)

win.mainloop()