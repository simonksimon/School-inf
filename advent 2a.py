game={("A","X"): 4, ("A","Y"): 5, ("A", "Z"): 9, ("B","X"): 3, ("B","Y"): 7, ("B","Z"): 11, ("C","X"): 5, ("C","Y"): 9, ("C","Z"): 10}
fr = open("advent 2a txt.txt","r")
suma = 0
for row in fr:
    chars = row.strip().split()
    suma += game[(chars[0],chars[1])]

print(suma)
