lines=int(input("input number of lines: "))
char=(input('input character: '))
type=(input('input type (S/F): '))
for i in range(lines):
  s=" "
  for m in range(lines-i):
    s=(f" {s}")
  if type=="S":
    for n in range(i):
      s = (f"{s} {char}")
  if type=="F":
    for o in range((i*2)-1):
      s = (f"{s}{char}")
  print(s)