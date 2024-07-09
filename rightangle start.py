'''n = int(input("please enter the no"))
for i in range(1, n+1):
    for j in range(1, i+1):
        print("* ", end="")
    print()'''

#second Approch
n = int(input("please enter the no"))
for i in range(1, n+1):
    print("* " *i)


