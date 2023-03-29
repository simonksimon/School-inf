import tkinter as tk
win=tk.Tk()

def pohybovac():
    canvas.move(o1,5,0)
    canvas.after(500,pohybovac)

def mixer(e):
    print("I have executed myself.")
    print("")
    zozobj=canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if 1 in zozobj:

        if canvas.itemcget(o1,"fill")=="green":
            canvas.itemccongig(o1,fill="cyan")
        #getter na farbu utvaru c1
        #ak je zelena bude cajan, inak green
        else:
            canvas.itemconfig(o1,fill="green")

canvas=tk.Canvas(win,width=500,height=500,bg="white")
o1=canvas.create_rectangle(50,50,250,250,fill="cyan")
k1=canvas.create_oval(250,250,500,500,fill="beige")

canvas.bind("<Button-1>",mixer)
pohybovac()
print(o1)
canvas.pack()
win.mainloop()
