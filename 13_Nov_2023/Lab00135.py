# Collections in Python --> Focus on Main Business Logic rather than Low Level Logics

# dic , tuple , set , Orderdict


#  Counter: A Counter is a dictionary subclass for
#  counting hashable objects. It is an unordered collection
#  where elements are stored as dictionary keys and their counts are stored as
#  dictionary values


from collections import Counter

cnt = Counter()
for word in ["red", "blue", "red", "green", "blue", "blue"]:
    cnt[word] = cnt[word] + 1
print(cnt)

#  OrderedDict --> An OrderedDict is a dictionary subclass that
#  remembers the order that keys were first inserted. The only difference between
#  dict and OrderedDict is that

from collections import OrderedDict

d = OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
for key, value in d.items():
    print(key, value)
# OP -->  a A
# OP -->  b B
# OP -->  c C


# Namedtuple

from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "gender"])

person = Person(name="Vishnu", age=30, gender="M")
print("Name", person.name) # OP : Name Vishnu
print("Age", person.age) # OP : Age 30
print("Gender", person.gender) # OP : Gender M
