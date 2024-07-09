import json

data = {"name": "kiran", "age": 50, "city": "Nashik", "contry": "india", "mob": 10452001}

#write a data to a json file named 'output,json file'
with open('output.json', 'w') as file:
    json.dump(data, file)

with open('output.json', 'r') as file:
    xyz = json.load(file)
print(xyz)
