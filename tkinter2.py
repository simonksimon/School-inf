import tkinter as tk
win=tk.Tk()

ct.pack()
c=tk.Entry(win)
c.pack

def executor():
    print(a.get(),b.get(),c.get())
    ka=int(a.get())
    kb=int(b.get())
    kc=int(c.get())
    d=kb**2 - 4*ka*kc
    if d<0:
        print("Doesn't have a solution within real numbers.")
    elif
