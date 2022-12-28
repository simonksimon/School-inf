#6, "I"     -> "IIIIII"
#5, "Hello" -> "HelloHelloHelloHelloHello"
input1a=6
input1b="I"
input2a=5
input2b="Hello"

def repeat_str(repeat, string):
    vys=string
    for i in range(repeat-1):
        vys=(vys+string)
    return (vys)

a=repeat_str(input1a,input1b)
print(a)
b=repeat_str(input2a,input2b)
print(b)