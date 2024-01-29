import tkinter as tk

def nacitaj_subor(nazov_suboru):
    with open(nazov_suboru, 'r') as f:
        data = f.readlines()
    return [line.strip() for line in data]

def vytvor_krizovka(data):
    krizovka = [line.split(' ')[1] for line in data]
    tajnicka = [line.split(' ')[1][int(line.split(' ')[0])-1] for line in data]
    return krizovka, tajnicka

def vykresli_krizovku(krizovka, tajnicka):
    root = tk.Tk()
    max_len = max([len(word) for word in krizovka])
    for i, line in enumerate(krizovka):
        for j in range(max_len):
            if j < len(line):
                char = line[j]
                if j == int(data[i].split(' ')[0])-1:
                    label = tk.Label(root, text=char, bg="yellow", relief="solid", bd=1)
                else:
                    label = tk.Label(root, text=char, relief="solid", bd=1)
                label.grid(row=i, column=j+max_len-int(data[i].split(' ')[0]))
    root.mainloop()

ver=input("Chceš verziu '1' alebo verziu '2'?")
data = nacitaj_subor('krizovka1-'+ver+'.txt')
krizovka, tajnicka = vytvor_krizovka(data)
vykresli_krizovku(krizovka, tajnicka)
