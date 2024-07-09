#program to reverse a given sentense
s = 'paras is good boy'
temp = s.split()
print(temp)
result = []
i = len(temp)-1
while i>= 0 :
    result.append(temp[i])
    i = i-1
print(result)
output = ' '.join(result)
print(output)
