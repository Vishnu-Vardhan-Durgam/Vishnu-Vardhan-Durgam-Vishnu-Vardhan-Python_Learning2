# Encapsulation

class BankAccount:
    def __init__(self):
        self.balence = 0  # Istance variable (you can access it)

    def deposite(self, amount):  # Public
        # self.balence = self.balence + amount
        self.balence += amount

    def _withdraw(self, amount):  # Protected
        self.balence -= amount

    def __show_balence(self):  # Private
        print("Your bal ", self.balence)

    def is_Auth(self, isAuth): # Public
        if isAuth:
            self.__show_balence() # Private
        else:
            print("You are not Auth")

    # def do_withdraw_by_bank_manager(self, amount):     # Public
    #     self._withdraw(amount=amount)                  # Protected


jp_chase = BankAccount()
jp_chase.deposite(1000)
jp_chase._withdraw(499)  # Not a good practive - protected
# jp_chase.__show_balence()

# Write the code to Auth
jp_chase.is_Auth(True)
