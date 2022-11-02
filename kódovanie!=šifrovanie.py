#zoberiem znak
#premením ho na číslo
#
#pripočítam k nemu ten posun
#vyďelit zvyšok po delení 26
#k výsleku pripočítať 97
#číslo previesť na znak
#tento proces spraviť pre kadžý znak v reťazci

#Cézarova šifra (spočíva v posune znakov v zadanom texte vždy o rovnakú zadanú číselnú hodnotu v abecede. Napríklad ak zadáte 'ahoj' a posun zvolíte
#1 potom sa všetky znaky v tomto slove posunú práve o jeden znak dopredu čiže vznikne 'bipk'.)
def Ceasar_encode(zdroj:str,posun:int)->str:
    a=len(zdroj)
    for i in range(a+1):
        if i<len(zdroj):
            b=len(abeceda)
            for y in range(b+1):
                if y<len(abeceda):
                    if zdroj[i]==abeceda[y]:
                        vys=(f"{vys}{abeceda[y+posun]}")
    print(vys)

abeceda="abcdefghijklmnopqrstuvwxyz"
vys=""
vstup=input("Čo chcete enkódnuť? ")
posunutie=input("O koľko má byť šifra posunutá? ")
vys2=Ceasar_encode(vstup,posunutie)

