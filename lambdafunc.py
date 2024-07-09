"""def cube(n):
    return n**3
print(cube(3))


f = lambda n:n**3
print(f(2))"""

# check no is even or odd
l = lambda x:'yes' if x%2 == 0 else 'no'
print(l(5))
print(l(10))

# Add two nos
s = lambda a,b: a+b
print(s(10,5))

#find even no from list usinf lambda using filter
lst = [10,2,55,2,12]

result = list(filter(lambda x:x%2==0, lst))
print(result)


#double the each element from list using lambda using map function
lst = [10,2,55,2,12]

result = list(map(lambda n:n**2, lst))
print(result)

# Sum of all the element from list using lambda using reduce function
from functools import reduce
lst = [10,5,5,30]

result = reduce(lambda x,y:x+y, lst)
print(result)

