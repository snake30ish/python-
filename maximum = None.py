maximum = None
minimum= None
while True:
    entry = input( 'give A  integer number ')
    if entry == 'done':
        break
    try:
        int_entry= int(entry)
        if maximum is None or maximum > entry:     
            maximum = entry
        if minimum is None or mimimum < entry:
            minimum = entry 
    except:ValueError:
        print ('Invalid input')
        continue
print ('Maximum is ',maximum)     
print ('Minimum is ,',minimum)   
