#s = '*'.join(['kk','ll','mm']) # to join the string

m = input("enetr the string")
#print(m[::-1]) # reverse a given string
#print(','.join(reversed(m))) # reverse a given string


i = len(m)-1
result = ''
while i>=0:
    result = result+m[i]
    i = i-1
print(result)
