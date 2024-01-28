# Father , Mother --> 5 , 5
# Multiple Inheritance


class Father:

    def father_money(self):
        return 5


class Mother:

    def mother_money(self):
        return 5


class Son(Father, Mother):
    pass


son = Son()
print(son.father_money()) # OP : 5
print(son.mother_money()) # OP : 5
