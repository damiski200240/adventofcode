import re

# in this code I will use the re library, I found the regex pattern by exploring the library's description on the internet
f = open('adventofcode_p3.txt', "r")
contenu = f.read()

pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"

list = re.findall(pattern, contenu)
# print(list)

sum = 0
for element in list: 
    numbers = element[4:-1] # we extract the numbers
    x, y = numbers.split(",")
    prod = int(x) * int(y) 
    sum += prod

print(sum) #169021493

# 2nd part

pattern_2nd = r"do\(\)|don't\(\)|mul\([0-9]{1,3},[0-9]{1,3}\)"

list_2nd = re.findall(pattern_2nd, contenu)

sum_2nd = 0

active = True
for element in list_2nd: 
    if element.startswith("do()"): 
        active = True
    elif element.startswith("don't()"): 
        active = False
    if element.startswith("mul(") and active: 
        numbers = element[4:-1] # we extract the numbers
        x, y = numbers.split(",")
        prod = int(x) * int(y) 
        sum_2nd += prod

print(sum_2nd) #111762583
