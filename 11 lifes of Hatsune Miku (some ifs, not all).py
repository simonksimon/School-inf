fr=open('Song the game of life.txt','r')

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
vratitpriatelov(1,0,oldfield)