set1={1,2,3,4,5,}
set2={6,7,8,9,10}
set1.add(9)
print(set1)
set1.remove(2)
print(set1)
print(set1.union(set2))
print(set1.intersection(set2))
print(set2-set1)
if 3 in set2:
    print(True)
else:
    print(False)