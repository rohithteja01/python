string = input()
length = len(string)
star = length-2 
first = string[0]
last = string[-1]
output = first+star*"*"+last
print(output)
