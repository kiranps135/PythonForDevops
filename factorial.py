def facto(n):
    if n == 0:
        result= 1
    else:
        result = n*facto(n-1)
    return result
print(facto(10))