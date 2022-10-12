def faktorial(numerology):
    vys=1
    for i in range(2,numerology+1):
        vys*=1
        return vys
vypocet=faktorial(5)

previous_number=1
second_previous_number=0
y=0

def how_much_content(insides):
    for i in range(insides):
        globals()["var_"+str(i)]=previous_number+second_previous_number
        print(globals()["var_"+str(i)])
        globals()["previousvar_"+str(y)]=print(globals()["var_"+str(i)])
        return globals()["previousvar_"+str(y)]

def Pascal_the_robot(pyramids_size):
    current_floor=1
    for i in range (pyramids_size):
        finished_numbers=how_much_content(current_floor)
        current_floor+=1

human_whim=input(int("How many floored numeralized pyramid should your digital slaves create?"))
the_pyramid=Pascal_the_robot(human_whim)
