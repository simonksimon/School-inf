import tkinter as tk
ver=input("Chceš verziu '1' alebo verziu '2'?")
with open('krizovka1-'+ver+'.txt', 'r') as f:
    d = f.readlines()

data=[]
for line in d:
    data.append(line.strip())
krizovka=[]
for line in data:
    krizovka.append(line.split(' ')[1])

root = tk.Tk()
max_len=0
for word in krizovka:
    if len(word)>max_len: max_len=len(word)
for i, line in enumerate(krizovka):
    for y in range(max_len):
        if y<len(line):
            char=line[y]
            if y==int(data[i].split(' ')[0])-1: label=tk.Label(root, text=char, bg="yellow", relief="solid")
            else: label=tk.Label(root, text=char, relief="solid")
            label.grid(row=i, column=y+max_len-int(data[i].split(' ')[0]))
root.mainloop()
