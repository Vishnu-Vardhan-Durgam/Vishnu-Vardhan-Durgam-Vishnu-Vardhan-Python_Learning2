# Single inheritance - 90%


# use the properties and methods of your base class or parent class by sub class

class Father:
    Bank_bal = 100

    def one_bhk(self):
        print("use it son")


class Son(Father):
    pass # I will write the code in future or skip


s = Son()
s.one_bhk()  # OP : use it son
print(s.Bank_bal)  # OP : 100
