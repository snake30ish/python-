def computepay(h, r):
    if h >40:
        payment = h * r
        over_time= (h-40) * 0.50*r
        gross_payment= payment + over_time
        return gross_payment
        
        
    else:
        normal_pay = r*h
        return normal_pay
hours= input( "give me the hours of work ")
float_hours= float(hours)
rate= float(input("give the rate of your payment"))
p = computepay(float_hours, rate)
print("Pay", p)
