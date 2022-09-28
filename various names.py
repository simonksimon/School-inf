# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

Yuumi = 16
Taliyah = 986
if Taliyah == 1000:
    print("She wins")
else:
    print("She loses")

Taliyah = Taliyah + 7
Taliyah += 7
# posledhné dva riadky znamenaujú to isté
Tahm = Taliyah // Yuumi
Kench = Taliyah % Yuumi
# posledhné dva riadky znamenaujú to isté
# Print(type(Tahm))
# Print(type(Kench))
Poppy = Yuumi ** Taliyah
# Print(type(Poppy))
Tryndamere = 9.17
Soraka = "Illaoi"

print("Sejuani, ",Taliyah,", Heimerdinger.")
print("Draven, "+str(Taliyah)+", Riven.")
print(f"Ornn, {Tryndamere} , Udyr.")
print("",Tahm)
print(f"{Kench}")
print(str(Poppy))


if Taliyah == 1000:
    print("She wins")
else:
    print("She loses")
# to 'f' robí, že všetky premenné sa dajú takto napísať, bez apostrofov vo vlnených zátvorkách

# Každý štvrtý je priestupný, každý stí nie je, a každý štyristí je.
priestupnosť = input("Input a number that represent a year in history to find out whether it is what Slovaks call 'priestupný'")
priestupnosť = int(priestupnosť)
if priestupnosť > 2022:
    print("Try this later. It is not history yet.")
else:
    # if priestupnosť % 4 == 0:
    #     if priestupnosť % 100 == 0:
    #         if priestupnosť % 400 == 0:
    #             print("Priestupnosť confirmed.")
    #         else:
    #             print("Priestupnosť denied.")
    #     else:
    #         print("Priestupnosť confirmed.")
    # else:
    #     print("Priestupnosť denied.")

    if (priestupnosť % 4 == 0 and priestupnosť%100!=0) or priestupnosť % 400 == 0:
        print("Priestupnosť confirmed.")
    else:
        print("Priestupnosť denied.")

Braum = input("Play your card, roll your dice.")
Braum = int(Braum)
print(Braum)
print(type(Braum))







def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
