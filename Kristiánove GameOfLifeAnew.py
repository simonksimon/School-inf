import tkinter as tk
win = tk.Tk()

file = open("gospel_glider_gun.txt","r")

line = file.readline()

height,width = line.split(" ")

height = int(height)
width = int(width)

w = 600
h = 600

ws = 15

canvas = tk.Canvas(win, height = h, width = w, bg = "white")
canvas.pack()

value = "none"

def kresligrid():
    count = h//ws
    for i in range(count):
        canvas.create_line(0,i*ws,w,i*ws)
    count = w//ws
    for i in range(count):
        canvas.create_line(i*ws,0,i*ws,h)
kresligrid()

def create2Dmatrix():
    temp = []
    matrix = []
    for row in file:
        for char in row:
            if char == "1":
                temp.append(1)
            if char =="0":
                temp.append(0)
        matrix.append(temp)
        temp = [ ]
    file.seek(0)
    file.readline()
    return matrix


oldfield = create2Dmatrix()

newfield = create2Dmatrix()

def vratitpriatelov(x,y,oldfield):
    count = 0
    #oldfield [y][x]
    if x<width-1 and oldfield[y][x+1] == 1:
        count += 1
    if x<width-1 and y<height-1 and oldfield[y+1][x+1] == 1:
        count += 1
    if y<height-1 and oldfield[y+1][x] == 1:
        count += 1
    if x>0 and y<height-1 and oldfield[y+1][x-1] == 1:
        count += 1
    if x>0 and oldfield[y][x-1] == 1:
        count += 1
    if x>0 and y>0 and oldfield[y-1][x-1] == 1:
        count += 1
    if y>0 and oldfield[y-1][x] == 1:
        count += 1
    if x<width-1 and y>0 and oldfield[y-1][x+1] == 1:
        count += 1
    return count

def prepis(oldfield, newfield):
    for y in range(height):
        for x in range(width):
            friends = vratitpriatelov(x,y,oldfield)
            if oldfield[y][x] == 1:
                if friends == 2 or friends == 3:
                    newfield[y][x] = 1
                elif friends < 2:
                    newfield[y][x] = 0
                elif friends > 3:
                    newfield[y][x] = 0
            elif oldfield[y][x] == 0:
                if friends == 3:
                    newfield[y][x] = 1
    return newfield

def kreslicells(oldfield,ws):
    canvas.delete("all")
    kresligrid()
    for y in range(height):
        for x in range(width):
            if oldfield[y][x] == 1:
                canvas.create_oval(x*ws,y*ws,(x+1)*ws,(y+1)*ws,fill="red")
def automatickost():
    global value
    value = "auto"
    canvas.after(100,generacie)

def manualnost():
    global value
    value = "manual"
    generacie()
    return value

def generacie():
    global oldfield,newfield
    kreslicells(oldfield,ws)
    newfield = prepis(oldfield,newfield)
    for y in range(height):
        for x in range(width):
            oldfield[y][x]= newfield[y][x]
    canvas.update()
    if value=="auto":
        automatickost()
        print(value)

button1 = tk.Button(win, text= "Auto",command = automatickost)
button1.pack()
button2 = tk.Button(win, text="Manual", command = manualnost())
button2.pack()

win.mainloop()

