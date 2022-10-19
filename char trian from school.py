character=input("What symbol?")
pocet=input("How many?")
def riadok(n,ret):
    ph=(n-len(ret))//2
    if ph%2==1:
        pph=ph+1
    else:
        pph=ph
    print(character*pph,end="")
    print(ret,end="")
    print(character*ph,end="")
riadok=(pocet,"Andrej Kmeť")
