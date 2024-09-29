try:
    hrs = input("Enter Hours:")
    h = float(hrs)
    rate = input ("give me the rate ")
    rate_float = float(rate)
except:
    print ( " only numeric values")
    quit()
    


if h >40:
    payment = h * rate_float
    over_time= (h-40) * 0.50*rate_float
    gross_payment= payment + over_time
else:
    gross_payment=h * rate_float
print (gross_payment)
     
   