maximum = None
minimum= None
while True:
    entry = input( 'give A  integer number ')
    if entry == 'done':
        break
    try:
        int_entry= int(entry)
        if maximum is None:
            maximum = entry
        elif entry > maximum:
            maximum = entry 
    except:
        print ('invalid input')
        continue
    
print ('the largest is',maximum)     
print ('the minimum is ,')   