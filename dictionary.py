dic = {1:"first",2:"second",3:"third"}
print(dic)
print(type(dic))
print(dic.items())
k=dic.keys()
for i in k:print(i)
v=dic.values()
print(v)
print(dic.get(1))
del dic[2]
print(dic)