# 1. What do we use these Linux commands for:
# ls: listing the contents of a directory
#  cd: navigation into a specific folder
# touch: create files
# pwd: prints out the current working directory

# 2. What do we use these operations for:
# a. *, b. +, c. **, d. //, e. % :
t = 17
h = 3
print(t*h)
print(t+h)
print(t**h)
print(t//h)
print(t%h)

# 3. Given x= 29, what is the value of x after the operation x%=4:
x = 29
x %= 4
print (x)

# 4. Given x=7, what is the result of the operation x**3:
x = 7
x **3
print(x)

# 5. Given variables; name ='Ashley', age=20, country='Rwanda',
# a. show how to print these sentences using String formatting:
name = "Ashley"
age = 20
country = "Rwanda"
sentence = f"{name}, {age}, {country}"
print(sentence)
# b. 'I am Ashley from Rwanda and I am 20 years old' :
d = f"I am {name} from {country} and I am {age} years old"
print(d)
# name2 = name.upper()
# c. 'My name is ASHLEY. I was born in 1994'
year = 1994
e = f"My name is {name.upper()}. I was born in {year}"
print(e)

# 6. Given p = 'Hello Python World' :
p = "Hello Python World"

# replace all occurences of 'o' with 'a':
print(p.replace('o', 'a'))
# length of the string p:
print(len(p))
# convert p into uppercase:
print(p.upper())
# convert p into lowercase:
print(p.lower())

# Print the first character of of each word using positive indexing:
print(p[0])
print(p[6])
print(p[13])

# print the last character of each word using negative indexing
print(p[-14])
print(p[-7])
print(p[-1])

# What negative number slicing combination returns:
# i. Hell
print(p[-18 : -14])
# ii. Py
print(p[-12 : -10])
# iii. on World
print(p[-8 : ])

# 7. Given i = 'I am 19 years old.' ; What do these strings checks return:
i = "I am 19 years old."
print(i.islower())
print(i.isalpha())
print(i.isalnum())
print(i.islower())
print(i.index('a'))
print(i.find('z'))

# 8. Given s = 'I love AkiraChix' ; What do these indexing and slicing operations return:
s = "I love AkiraChix"
print(s[0])
print(s[3])
print(s[-5])
print(s[-12])
print(s[4:11])
print(s[-10:-5])
print(s[-4:])
print(s[-14:6])



