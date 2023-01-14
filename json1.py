import json

data = open('json1.json')

def replacer(key,val):
    if key == "email":
        return "undefined"
    else:
        return val

# "info" as a dictionary in python after we load the json
info = json.load(data)
print("name:", info["name"])
print("phone:",info["phone"]["number"])
print("email:",replacer("email", info["email"]["val"]))