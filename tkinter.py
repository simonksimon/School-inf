import tkinter as tk
win=tk.Tk()

def executor():
    print("Stalo sa.")

button = tk.Button(win,text="Press me...",command=executor)
button.pack()

win.mainloop()
