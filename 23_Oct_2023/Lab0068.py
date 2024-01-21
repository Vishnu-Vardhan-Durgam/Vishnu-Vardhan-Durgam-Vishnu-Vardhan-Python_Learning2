# def sayHello(name):
#     print("Hello How are you" , name)

# or

sayHello = lambda name: print("Hello, How are you", name)

sayHello("vishnu")


################

def funcwithParam(a):
    return a ** 2


op = funcwithParam(2)
print(op)


#####################
# lambda expression

# def doubleOfMe(value):
#     return value * 2


# output = doubleOfMe(2)

# or

output = lambda value: value * 2


print(output(2))


