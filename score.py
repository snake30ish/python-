score = float(input("Enter Score: "))
if score < 0:
    print("error only between 0-1") 
elif score >1:
    print ("error only between 0-1")
elif score >= 0.9: 
    print( "A")
elif score >= 0.8:    # try grade 0.89
    print("B")
elif score >= 0.7:
    print ( "C")
elif score >= 0.6:
    print ("D")
else:
    print("F")