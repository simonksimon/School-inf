import tkinter as tk
import random
win=tk.Tk()
head=[500//2,500//2]
mv=[0,-1]
speed=100
#whole_snake=[head]
canvas=tk.Canvas(width=500, height=500, bg="white")
canvas.pack()
ihruskaf=False
hrusiz=10
hrunum=0

def draw_snake():
    global head,mv,speed,whole_snake,hruska,hrucou,hrunum,ihruskaf
    whole_snake=canvas.create_rectangle(head[0],head[1],head[0],head[1],fill="black")
    overlap = canvas.find_overlapping(head[0], head[1], head[0], head[1])
    head[0]+=mv[0]
    head[1]+=mv[1]
    if len(overlap)>1 and hruska in overlap:
        canvas.delete(hruska)
        canvas.delete(hrucou)
        hrunum += 1
        ihruskaf = False
        hrusky()
    elif len(overlap)>1:
        canvas.delete("all")
        canvas.create_text(500 // 2, 500 // 2, text="You just killed one little snake. But don't worry. Your own life will continue. Just with that guilt.")
    else:
        canvas.after(speed,draw_snake)

def menic(e):
    global mv,speed
    print("I (not you) have clicked.")
    if e.char=="w":
        mv=[0,-1]
    elif e.char=="a":
        mv=[-1,0]
    elif e.char=="d":
        mv=[1,0]
    elif e.char=="s":
        mv=[0,1]
    elif e.char=="k":
        speed-=10
    elif e.char=="l":
        speed+=10

def hrusky():
    global ihruskaf,hrunum,whole_snake,hruska,hrucou,hrunum,ihruskaf
    if ihruskaf==False:
        hrucou=canvas.create_text(400, 480, fill="darkblue", font="Times 15", text="Odtrhnuté hrušky: "+str(hrunum))
        hruran1=random.randint(10,490)
        hruran2=random.randint(10,470)
        hruska=canvas.create_oval(hruran1,hruran2,hruran1+hrusiz,hruran2+hrusiz,fill="green")
        ihruskaf = True
        draw_snake()

draw_snake()
hrusky()
win.bind("<KeyPress>",menic)
win.mainloop()
