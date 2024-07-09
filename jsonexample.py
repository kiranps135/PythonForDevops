import json

# convert json data into dict
json_data = '{"name":"kiran","age": 29 , "city": "Nashik"}'
data = json.loads(json_data)

print(data)

data["contry"] = "india"
data["age"] = 50
data["mob"] = 10452001

print(data)
# convert dict data into json
json_updated_data = json.dumps(data)
print(json_updated_data)