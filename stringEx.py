ex = 'this is a string'
print(ex)
ex = "string examples"
print(ex)
print(r'C:\some\name')

s = '   You are awesome       '
#accessing index value
print(s[0])

#appending string no of times
print(s*3)

#lenght of String
print(len(s))

#slicing String
print(s[0:])
print(s[:-1])
print(s[-3:-1])

#0 starting index ,9 ending index , 2 interval travesal value
print(s[0:9:2])

#reverse a string
print(s[::-1])
print(s[3:0:-1])

#remove leading spaces
print(s.strip())
print(s.lstrip())
print(s.rstrip())

#find substring index
#it couldn't find substring return -1
print(s.find("awe"))
print(s.find("awe"),0,len(s))
print(s.find("awe",0,len(s)))

#count and replace
print(s.count("a"))
print(s.replace("awesome","super",0))

print(s.upper())
print(s.lower())
print(s.title())
