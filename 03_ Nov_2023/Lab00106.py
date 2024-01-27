class Car:
    colour = None
    model = None

    def car_details(self):
        print("Your car details are -->", self.colour, self.model)

car_colour = input("Enter your car colour \n")
car_model = input("Enter your calr model \n")

car_obj_ref = Car()
car_obj_ref.colour = car_colour
car_obj_ref.model = car_model

car_obj_ref.car_details() # OP : Your car details are --> tata v9
