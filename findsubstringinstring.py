s = 'hello my nake is kiran i am kiran i good name is kiran hi kiran'
subs = 'kiran'
found = False
pos = -1
length = len(s)
while True:
    pos = s.find(subs, pos+1, length)
    if pos == -1:
        break
    print("Found the sub string " , pos)
    found = True
if found == False:
    print("substring is not found")