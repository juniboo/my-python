from math import sin


digits = [1,2,3,4,5,6,7,8,9]
s = lambda x :x+sin(x)
print(list(map(s,digits)))
# List Comprehension
is_even = [1,2,3,4,5,6,7,8,9,10]
var = [x ** 2 for x in is_even if x // 2]
print(var)
char =[char.upper() for char in "hello world" if char != " "]
print(char)
#Function Combination in Functional Programming
s = filter(lambda x:len(x)>5,["hello", "world","phone","promise","application"],)
map(str.upper,s)
print(list(map(str.upper,s)))
