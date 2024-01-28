# Multilevel inheritance

# Level Grand father --> Father --> Son

class Grandparent:

    def grandparent_method(self):
        return ("Grandparent's method")


class Parent(Grandparent):

    def parent_method(self):
        return "Parent's method"


class Child(Parent):

    def child_method(self):
        return "Child's method"
    

parent = Parent()
child = Child()

print(parent.grandparent_method()) # OP : Grandparent's method

print(child.grandparent_method()) # OP : Grandparent's method
print(child.parent_method())  # OP : Parent's method
print(child.child_method())  # OP : Child's method
