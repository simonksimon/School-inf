Import tkinter as Tk
win=tk.Tk()
head=(500//2,50//2)
mv=[0,-1]
speed=100
whole_snake=[head]
canvas=tk.Canvas(width=500, height=500, bg="white")
canvas.pack()

def draw_snake():
    global head
    canvas.create_rectangle(head[0],head[1],head[0]+1,head[1]+1,fill="black")
    head[0]+=mv[0]
    head[1]+=mv[1]
    canvas.after(speed,draw_snake)

def menic(e):
    global mv,speed
    print("I (not you) have clicked.")
    if e.char="w":
        mv=[0,-1]
    elif e.char=="a":
        mv=[-1,0]
    elif e.char=="d":
        mv=[1,0]
    elif e.char=="s":
        mv=[0,1]
    elif e.char=="s":
        speed-=10
    elif e.char=="s":
        speed+=10

draw_snake()
win.bind("<>")