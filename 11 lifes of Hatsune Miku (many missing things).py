fr=open('Song the game of life.txt','r')

def kresligrid():
    count=HeighT//ws
    for i in range(count):
        canvas.create_linew(0,i*ws,WidtH,i*ws)
        count=WidtH//ws
        for i in range(count):
            canvas.create_line

    def kreslicells(oldfield,celllsit,ws):
        for item in celllist:
            canvas.delete(item)
        celllist=[]
        for y in range(height):
            for x in range(width):
                if oldfield[y][x]=1:


def create2Dmatrix(width,height):
    matrix=[]
    temp=[]
    for y in range(height):
        temp=[]
        for x in range(width):
            temp.append(0)
        matrix.append(temp)
    return matrix

def processfile():
    x=0
    y=0
    for row in fr:
        x=0
        for char in row:
            if char=="1":
                matrix[y][x]=1
            x+=1
        y+=1

def vratitpriatelov(x,y,matrix):
    count=0
    #matrix[x][y]
    if x>0 and y>0 and matrix[y-1]

    if x<(width-1) and y<(height-1) and matrix[y+1][x - 1]:

    return count

def prepis(oldfield,newfield):
    #cyklus v cykle a ifíky
    for y in range(height):
        for x in range(width):
            if:

width, height = fr.readline().split(" ")
width=int(width)
height=int(height)
#vytvorí 2-rozmerný zoznam plný núl
oldfield=create2Dmatrix(width,height)
#vytvorí iný 2-rozmerný zoznam plný núl
newfield=create2Dmatrix(width,height)
#do prvého zoznamu nahodíme jednotky zo súboru
#processfile(oldfield)

def generacie():
    global oldfield, newfield
    print(oldfield)
    kreslicells(oldfield,celllist,30)
    #vypočítaš nový matrix
    rewrite(oldfield,newfield)
    for y in range(height):
        for x in range(width):
            oldfield[y][x]=newfield[y][x]
    #nový musíš vynulovať
    newfield=create2Dmatrix(width,height)
    canvas.after(100,generacie)

vratitpriatelov(1,0,oldfield)

generacie()
win.mainloop()