import json

x = {
    "firstname" : "Valentine",
    "lastname" : "Eze",
    "phonenumber" : "08160501383",
    "Address" : "Dreamlink Mile 50"
}

y = json.dumps(x)
print(x)
print(y)