def summary (x,y):
    apotelesma= x+y
    print (apotelesma)
    



def prakseis (a,b):
    afairesi= a-b
    pollaplasiasmos= a*b
    if b!=0:
        diairesi= a/b
    else:
        print (" divide by zero is imposible ")
    return print (" h afairesi einai",afairesi, "o pollaplasiasmos einai",pollaplasiasmos, "h diairesi einai ", diairesi)


prakseis(10,2)