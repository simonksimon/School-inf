jazykolam="Sedí mucha na stene. sedí a spí. Sedí a buvinká p*tvora malinká."
nie_spoluhlasky="aeiyou"
whoworkswithwords=input("Ktorú nespoluhlásku si celý svoj život hľadal?")
anti_not=" "
for i in jazykolam:
    if i in nie_spoluhlasky:
        anti_not=anti_not+whoworkswithwords
    else:
        anti_not=anti_not+i
print(anti_not)
