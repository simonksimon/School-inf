import tkinter as tk
win=tk.Tk()

at = tk.Label(win,text = "Coefficient a:")
at.pack()
a = tk.Entry(win)
a.pack()
bt = tk.Label(win,text = "Coefficient b:")
bt.pack()
b = tk.Entry(win)
b.pack()
ct = tk.Label(win,text = "Coefficient c:")
ct.pack()
c=tk.Entry(win)
c.pack()

def executor():
    print(a.get(),b.get(),c.get())
    ka=int(a.get())
    kb=int(b.get())
    kc=int(c.get())
    d=kb**2 - 4*ka*kc
    t2=""
    if d<0:
        t="Doesn't have a solution within real numbers."
    elif d==0:
        t=("Root is: ",str(-1*kb/(2*ka)))
    else:
        t=("Solution 1 is:", ((-1*kb+d**0.5)/(2*ka)), "and solution 2 is:", ((-1*kb-d**0.5)/(2*ka)))
    et = tk.Label(win, text=t)
    et.pack()
    e = tk.Entry(win)

button = tk.Button(win,text = "Click me !!",command = executor)
button.pack()

win.mainloop()