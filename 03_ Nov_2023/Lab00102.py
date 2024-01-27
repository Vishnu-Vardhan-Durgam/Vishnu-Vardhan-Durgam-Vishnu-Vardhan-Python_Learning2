# Car
# Objects - Tesla , Lambo , TATA

class Car:
    name = None
    colour = None
    model = None
    speed = None
    engine = None

    # self is a special variable that is used  within the context OOP's
    # it is a reference to te instance of a class
    # access and manipulate the attributes and methods of that instance / Object

    def start_engine(self):
        print("Starting engine")

    def drive(self):
        print("Drive")

    def car_break(self):
        print("Break -->" + self.name)

    def who_is_driving(self):
        print("I'm driving -->" + self.name)


tesla_obj_ref = Car()  # This is instance of a class - object
lambo_obj_ref = Car()  # This is instance of a class - object
tata_obj_ref = Car()  # This is instance of a class - object

tesla_obj_ref.name = "Tesla"
lambo_obj_ref.name = "Lambo"
tata_obj_ref.name = "TATA"

tesla_obj_ref.who_is_driving() # I'm driving -->Tesla
lambo_obj_ref.who_is_driving() # I'm driving -->Lambo
tata_obj_ref.who_is_driving() # I'm driving -->TATA

tesla_obj_ref.car_break() # Break -->Tesla
lambo_obj_ref.car_break() # Break -->Lambo
tata_obj_ref.car_break() # Break -->TATA
