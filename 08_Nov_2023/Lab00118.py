# Hybrid Inheritance

# Multiple types of inheritance such as single , multiple and multilevel inheritance

class A:

    def methodA(self):
        return "Method A"


class B(A):

    def methodB(self):
        return "Method B"


class C(A):

    def methodC(self):
        return "Method C"


class D(B, C):

    def methodD(self):
        return "Method D"

d = D()
print(d.methodA()) # OP : Method A
print(d.methodB()) # OP : Method B
print(d.methodC()) # OP : Method C
print(d.methodD()) # OP : Method D
