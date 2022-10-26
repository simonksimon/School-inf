from decimal import *

zvstup = False
while zvstup==False:
  pcislica = 0
  dcislica = 0
  vysledok = 0
  operator = '+'
  dcislo=0
  done = True

  vstup=str(input("Napíš príklad na + alebo -: "))

  b=len(vstup)
  for i in range(b+1):
    if i<len(vstup):
      ch=vstup[i]
    else:
      ch='+'
    if (ch >= '0' and ch <= '9') or ch == '.' or ch == 'e':
      if done==True:
        pcislica = i
        done = False
      dcislica = i
    else:
      if done==False:
        dcislo = Decimal(vstup[pcislica:dcislica+1])
        if operator=='+':
          vysledok = vysledok + dcislo
        if operator=='-':
          vysledok = vysledok - dcislo
        done = True
      if ch == '+' or ch == '-':
        if operator == '-' and ch == '-':
          operator = '+'
        else:
          operator = ch
      else:
        print("Zlý vstup.")
        zvstup=True
  if zvstup==False:
      print(vysledok)
