# Method Overloading
# Python doesnot support Method Overloading in traditional sence


class MathUtil():
    def add(self, a, b=0, c=0):
        print(a + b + c)

    # def add(self, a, b, c):
    #     print(a + b + c)


math = MathUtil()
op1 = math.add(1)   # OP : 1
op2 = math.add(1, 2)    # OP : 3
op3 = math.add(1, 2, 3)    # OP : 6


