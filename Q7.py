def Clean(InString):
    AfterSpace = False
    NewString = ""
    for i in range (len(InString)):
        NextChar=InString[i]
        if AfterSpace == True:
            if NextChar !=" ":
                NewString=NewString + NextChar
                AfterSpace=False
        else:
            NewString=NewString+NextChar
            if NextChar==" ":
                AfterSpace=True
    return NewString

print(Clean("x   y and  z"))
