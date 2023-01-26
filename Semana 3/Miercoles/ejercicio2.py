personal_data = {
    "name" : input("Please enter your name:"),
    "age" : input("Please enter your age:"),
    "address" : input("Please enter your address:"),
    "phone" : input("Please enter your phone number:")
}

print(f"{personal_data.get('name')} tiene {personal_data.get('age')} años, vive en {personal_data.get('address')} y su número de teléfono es {personal_data.get('phone')}")
personal_data2 = {}

name = input("Please enter your name:")
age = input("Please enter your age:")
address = input("Please enter your address:")
phone = input("Please enter your phone number:")

personal_data2["name"] = name
personal_data2["age"] = age
personal_data2["address"] = address
personal_data2["phone"] = phone

print(f"{personal_data2.get('name')} tiene {personal_data2.get('age')} años, vive en {personal_data2.get('address')} y su número de teléfono es {personal_data2.get('phone')}")

name = input("Please enter your name:")
age = input("Please enter your age:")
address = input("Please enter your address:")
phone = input("Please enter your phone number:")

personal_data3 = {
    "name" : name,
    "age" : age,
    "address" : address,
    "phone" : phone
}
print(f"{personal_data3.get('name')} tiene {personal_data3.get('age')} años, vive en {personal_data3.get('address')} y su número de teléfono es {personal_data3.get('phone')}")
