class Myclass:
    name = None
    last_name = None

    def print_my_name_with_last_name(self, last_name, age , state):
        print("Your name is --> " + self.name, last_name , age , state)


pramod_obj_ref = Myclass()
pramod_obj_ref.name = "Vishnu"
pramod_obj_ref.print_my_name_with_last_name("Dutta",25 , "HYD") # OP : Your name is --> Vishnu Dutta 25 HYD
