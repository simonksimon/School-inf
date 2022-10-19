def pigspeech(slovo:str)->str:
    novoslovo=""
    if len(slovo)>3:
        novoslovo=slovo[1::]+slovo[0] #/[:1:] /[0::]
        novoslovo+="ya"
        #novoslovo=(f"{novoslovo}ya")
    else:
        novoslovo=slovo
    return novoslovo
