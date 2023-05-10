# gulicka cez create_oval treba ju posuvat o dany vektor
# move(vector) posun o dany vektor
# vector(1,1) -> vector(-1,1) -> vector(-1,-1) -> vector(1,-1) -> vector(1,1)
import tkinter as tk
from random import randrange

def ball_move():
    global ball, movement, desk
    canvas.move(ball, movement[0], movement[1])
    pos = canvas.coords(ball)
    desk_pos = canvas.coords(desk)
    overlap = canvas.find_overlapping(desk_pos[0], desk_pos[1], desk_pos[2], desk_pos[3])
    if pos[2] >= width:     # prava hranica
        # movement = [-1, 1]
        movement = [movement[0] * -1, movement[1]]
        # faker(0)
    elif pos[3] >= height:  # spodna hranica
        canvas.delete('all')
        text = canvas.create_text(width//2, height//2, text='YOU LOST')
    elif pos[0] <= 0:       # lava hranica
        # movement = [1, -1]
        movement = [movement[0] * -1, movement[1]]
        # faker(0)
    elif pos[1] <= 0:       # vrchna hranica
        # movement = [1, 1]
        movement = [movement[0], movement[1] * -1]
        # faker(1)
    elif ball in overlap:
        # movement = [-1, -1]
        # faker(1)
        movement = bounce(pos, desk_pos)
    canvas.after(4, ball_move)


def faker(a):   # nepotrebny lebo uhol sa meni pri odraze od rectanglu
    global movement
    d = randrange(-1, 2)
    movement[a] += d


# def move_left(e):
#     canvas.move(desk, -4, 0)


# def move_right(e):
#     canvas.move(desk, 4, 0)


def mover(e):
    global x
    x2 = e.x
    if x != 0:
        mouse = x2-x
        canvas.move(desk, mouse, 0)
        x= e.x


def bounce(ball_pos, rec_pos):
    ball_pos = (ball_pos[0] + ball_pos[2])//2
    rec_middle = (rec_pos[0] + rec_pos[2])//2
    ball_to_rec = ball_pos - rec_middle
    return [ball_to_rec//(rec_w//3), -1]    # rec_w//3 => vector x je 0-3


def starter(e):
    global x, y
    zoz = canvas.find_overlapping(e.x, e.y, e.x+1, e.y+1)
    if desk in zoz:
        x = e.x
        y = e.y
        ball_move()
        canvas.delete(start_text)


root = tk.Tk()
width = 500
height = 500
ws = 10
rec_w = 25
canvas = tk.Canvas(root, width= width, height= height, bg= 'white')
canvas.pack()
movement = [0,1]
ball = canvas.create_oval(width//2 - ws, height//2 - ws, width//2 + ws, height//2 + ws, fill = 'red')
desk = canvas.create_rectangle(width//2 - rec_w, height - 30, width//2 + rec_w, height - 20, fill= 'yellow')
start_text = canvas.create_text(width//2, height//2 - 50, text='CLICK ON RECTANGLE TO START\nplay on fullscreen\nuse mouse to move')

# treba najst bind na sipky
canvas.bind('<Button-1>', starter)
canvas.bind('<Motion>',mover)
# canvas.bind('d',move_right)

root.mainloop()