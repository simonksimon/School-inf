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

# -----------------------------------
# ALGORITMUS !!!!!
# -----------------------------------
# string
# - pismena? nie
# - specialne znaky? ano : dva : plus a minus
# - cisla ? ano
#
# premenne
# -vstup
# -prva cislica
# -druha cislica
# -vysledok
# -operator
# -druhe cislo
# -done
#
# 'inicializacia
# prva cislica = 0
# druha cislica = -1
# vysledok = 0
# operator = '+'
# druhe cislo = 0
# done = true
#
# loop at vstup into ch
# if ch >= '0' and ch <= '9'
#   if done
#     prva cislica = aktualna pozicia
#     done = false
#   endif
#   druha cislica = aktualna pozicia
# else
#   if not done
#     druhe cislo = int(vstup[prva cislica .. druha cislica])
#     case operator:
#       '+': vysledok = vysledok + druhe cislo
#       '-': vysledok = vysledok - druhe cislo
#     endcase
#     done = true
#   endif
#
#   if ch = '+' or '-'
#     operator = ch
#   else if ch = ' '
#     ' literally do nothing
#   else
#   error 'zly vstup'
#   endif
# endif
# endloop