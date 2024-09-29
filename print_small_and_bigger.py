maximum = None
minimum= None
while True:
    entry = input( 'give A  integer number ')
    if entry == 'done':
        break
    try:
        int_entry= int(entry)
        if maximum is None or int_entry > maximum:     
            maximum = int_entry
        if minimum is None or int_entry < minimum:
            minimum = int_entry 
    except ValueError:
        print ('Invalid input')
        continue

print ('Maximum is', maximum)     
print ('Minimum is', minimum)