def duplicate_count(text):
    # Your code goes here
    zoz=[]
    vys=0
    zoz2=[]
    a=""
    y=""
    numbers=" 0123456789"
    for i in range(len(text)):
            a=str(text[i])
            if a not in numbers:
                y=a.lower()
            if y not in zoz:
                if y not in zoz2:
                    zoz.append(text[i])
            elif y in zoz:
                 if y not in zoz2:
                    vys=vys+1
                    zoz2.append(text[i])
    return (vys)

#input="kHYbPOA2UqmFW5TjsbvYpZzfWOkSXcYjXgPwzqSC0"
input="a5G6Qq2qUCSV7T97PXMS3viLwD1bs6xGMBDGmIawalKlJNuYFJtJJd74o60W7WYrC3EOu0i4a37NRVSh1N"
print(duplicate_count(input))