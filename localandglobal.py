x = 100
def cal():
    x=11
    print(x)
    print(globals()['x'])

print(x)
z = cal
z()
z()
z() 