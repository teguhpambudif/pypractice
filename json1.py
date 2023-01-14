import json

data = open('json1.json')

def replacer(key,val):
    if key == "email":
        return "undefined"
    else:
        return val

info = json.load(data)
print("name:", info["name"])
print("phone:",info["phone"]["number"])
print("email:",replacer("email", info["email"]["val"]))
# print(info["email"]["val"])