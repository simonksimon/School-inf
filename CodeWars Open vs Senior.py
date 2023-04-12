def open_or_senior(data):
    output=[]
    after=False
    done=False
    for i in range(len(data)):
        current=str(data[i])
        age=""
        handicap=""

        for y in range(len(current)):
            if current[y]==",":
                for z in range(y-1):
                    age=(age+current[z+1])
        gap=len(current)-(len(age)+2)
        for z in range(gap):
            handicap=(handicap+current[len(age)+z+2])

        if int(age)>54:
            if handicap[0]!="-":
                handycap=int(handicap)
                if handycap>7:
                    output.append("Senior")
                else:
                    output.append("Open")
                    done=True
            else:
                if done==False:
                    output.append("Open")
                    done=True
        else:
            if done==False:
                output.append("Open")
    return output

input=[(3, 12),(55,1),(91, -2),(54, 23)]
out=open_or_senior(input)
print(out)
