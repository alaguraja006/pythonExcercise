s= {'wssf',10,54,1,3,10,4}
print(s)
s.update([-1,99,1000])
print(s)
s.remove(10)
print(s)

#frozoneSet
f= frozenset(s)
print(f)