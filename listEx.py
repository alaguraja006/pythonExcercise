ls = [10,20,'hai',-10,23.03]
print(ls)
print(ls[3])
print(ls[3:5])
print(ls*3)
print(len(ls))
print(ls[::-1])

ls.append(40)
print(ls)
ls.remove('hai')
print(ls)
del(ls[1])
print(ls)
ls.insert(1,1000)
ls.sort()
print(ls)
ls.sort(reverse=True)
print(ls)
print(max(ls))
print(min(ls))


ls.clear()
print(ls)