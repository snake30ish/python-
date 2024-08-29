lists=[]
for number in range(1,11):
    lists.append(number)
lists.append(11)
print(lists)
lists.pop(0)
print(lists)
lists.sort(reverse=True)
print(lists)
print(sum(lists))
print (sum(lists)/len(lists))
# the hard way of mean...
print((lists[0]+lists[1]+lists[2]+lists[3]+lists[4]+lists[5]+lists[6]+lists[7]+lists[8]+lists[9]) / len(lists))
