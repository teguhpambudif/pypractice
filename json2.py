import json

data = open('json2.json')

info = json.load(data)
print("User count:", len(info),"\n")

for item in info:
    print('Name:',item["name"])
    print('Id:',item["id"])
    print('Attribute:',item["x"])
    print("======")