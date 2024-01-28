# Encapsulation

class Password:
    def __init__(self, password):
        self.__password = password

    def get_password(self,is_Auth):
        if is_Auth:
            return self.__password
        else:
            print("Error")

    def set_password(self,password):
        if len(password) > 10:
            self.__password = password
        else:
            print("Weak Password")

    def print_len(self):
        print("Your password len is", len(self.__password))


pwd = Password("Hacker123")
pwd.print_len()  # OP : Your password len is 9
pssd = pwd.get_password(True)
print(pssd)  # OP : Hacker123

pwd.set_password("Vishfu1yusdfxu23")
pwd.print_len()
