phone_book = {"batman": 98376267, "superman": 23648764, "wonder": 8736463}

# dict is closer to JSON

print(phone_book)
print(len(phone_book))
print(phone_book["batman"])
print(phone_book["wonder"])

# you can access element by key only - Dict
#################################################################
# second type  of dict

phone_book2 = dict(batman=1234, cersie=4763, GB=12347)
print(phone_book2)
print(phone_book2["cersie"])  # OP =  4763
print(phone_book2.get("cersie"))  # OP = 4763
print(phone_book2["GB"])  # OP = 12347
print(phone_book2.get("GB"))  # OP = 12347

#################################################################

# vishnu_details = dict(name="Vishnu", age=25, isMale=True, address="HYD")
vishnu_details = {"name": "Vishnu", 90: 25,"age" : 30 ,"isMale": True, "address": "HYD"}
print(vishnu_details)
print(vishnu_details)
print(vishnu_details[90])
print(vishnu_details["age"])
print(vishnu_details.get("address"))
