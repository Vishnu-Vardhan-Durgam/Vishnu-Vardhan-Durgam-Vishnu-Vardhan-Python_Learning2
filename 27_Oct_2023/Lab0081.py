tuple = tuple(["sachin", "virat", 12.36])

print(tuple[0])  # OP = sachin
print(tuple[1])  # OP = virat
print(type(tuple[2]))  # OP = <class 'float'>
print("-----")

# merging tuples

cricketers1 = ("sachin", "sehwag", "ganguly")
cricketers2 = ("dhoni", "virat", "rohit")

team_india = cricketers1 + cricketers2
print(team_india)  # OP = ('sachin', 'sehwag', 'ganguly', 'dhoni', 'virat', 'rohit')

# convert to list

list1 = list(team_india)
print(list1)  # OP = ['sachin', 'sehwag', 'ganguly', 'dhoni', 'virat', 'rohit']
print(type(list1))  # OP = <class 'list'>
print("------")

x = 10
a, b = 10, 20  # this is multiple value asssign
q, r, s = 15, 30, 45  # tuple assigned to multiple variables
print(q)  # OP = 15
print(r)  # OP = 30
print(s)  # OP = 45

# nested tuples
cricketers3 = ("sachin", "sehwag", "ganguly")
cricketers4 = ("dhoni", "virat", "rohit")
team_india1 = cricketers1, cricketers2
print(team_india1)  # OP = (('sachin', 'sehwag', 'ganguly'), ('dhoni', 'virat', 'rohit'))
print(team_india1[0])  # OP = ('sachin', 'sehwag', 'ganguly')
print(team_india1[0][0])  # OP = sachin
print(team_india1[0][1])
print(team_india1[0][2])
print(team_india1[1])  # OP = ('dhoni', 'virat', 'rohit')
print(team_india1[1][0])  # OP = dhoni
print(team_india1[1][1])
print(team_india1[1][2])
print("======")

# search in tuple

cities = ("mumbai", "hyderabad", "chennai", "delhi")
print("mumbai" in cities)
print("chennai" in cities)
print("banglore" in cities)
