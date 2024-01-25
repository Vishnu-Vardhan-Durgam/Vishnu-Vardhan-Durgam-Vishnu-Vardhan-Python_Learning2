products = [
    {"name": "Laptop", "price": 1000},
    {"name": "smartphone", "price": 500},
    {"name": "Tablet", "price": 300},
    {"name": "Headphones", "price": 100},

]
print(type(products))  # op : <class 'list'>
print(type(products[0]))  # op : <class 'dict'>


def is_affordable(item):
    return item["price"] < 500


affordable_items = list((filter(is_affordable, products)))

# for i in affordable_items:
#     print(i["price"],i["name"]) # OP : 300 Tablet & 100 Headphones

print(affordable_items)  # op : [{'name': 'Tablet', 'price': 300}, {'name': 'Headphones', 'price': 100}]

print(affordable_items[0]["name"] + str(affordable_items[0]["price"]))  # op : Tablet300
print(affordable_items[1]["name"] + str(affordable_items[1]["price"]))  # Headphones100
