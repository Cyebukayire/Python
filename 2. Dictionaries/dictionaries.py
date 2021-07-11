customers = {        
    "name": "Peace Hanson",
    "age": 18,
    "is_verified": True
}

# ways to access value of a key in a dictionary
print(customers["name"], customers.get("friend", "Ketty Kelly"))
# get method above won't create new key in customers dictionary

# re-assign the key
customers["name"] = "Pretty Ketty"
print(customers.get("name"))