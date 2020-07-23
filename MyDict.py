import json
from difflib import get_close_matches
x=json.load(open("data.json","r"))
def translate(w):
    w=w.lower()
    y=w.capitalize()
    z=w.upper()
    if w in x.keys():
        return x[w]
    elif y in x.keys():
        return x[y]
    elif z in x.keys():
        return x[z]
    else:
        a=get_close_matches(w,x.keys(),n=1)
        print("dont get that word is it '%s'"%a[0])
        b=input("enter y/n : ")
        if b.lower()=="y":
            return x[a[0]]
        elif b.lower()=="n":
            return "sorry we didn't get that"
        else:
            print()
            return "Sorry, unrecognized word"

print("\t\t\t Welcome to interactive dictionary")
while True:    
    word=input("enter word : ")
    print()
    output=translate(word)
    if type(output)==list:
        for i in range(len(output)):
            print(i+1,". ",output[i])
    else:
        print(output)
    y=input("\nWant to ask more y/n : ")
    print("")
    if y=="n":
        print("\t\t\t_____THANK YOU_____")
        break
    elif y!="y":
        print("I'll take it as yes")
        
