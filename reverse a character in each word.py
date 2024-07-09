#reverse a string with each character words
'''s = 'paras is good boy'
temp = s.split()
print(temp)
i = len(temp)-1
result = []
while i>= 0:
    #a = i[::-1]
    result.append(temp[i][::-1])
    i = i-1
print(result)
output = ''.join(result)
print(output)
'''
#reverse a character in each word of string
s = 'python is cool'
temp = s.split()
print(temp)
result = []
i = 0
while i < len(temp):
    result.append(temp[i][::-1])
    i = i+1
print(result)
output = ''.join(result)
print(output)

