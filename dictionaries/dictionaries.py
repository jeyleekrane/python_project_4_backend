private_keys = {"username": "stanley", "password": "c9mxqkj*81weik", "DOB": "12-12-12",
                "Marital_Status": "Maried", "No_of_kids": 4, "Address": "No123, Shagamu Estate", }
print(private_keys.keys())
print(private_keys.values())

for private_key in private_keys:
    print(private_key, private_keys[private_key])
