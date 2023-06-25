# Module 03 Lab
# Thomas Gordon
# Program defines a class of Vehicle, and a Subclass of Automobile, then loops through a list of questions for the user to define a new instance of Automobile

class Vehicle:
    def __init__(self, v_type):
        self.v_type = v_type
    def __str__(self):
        return f"{self.v_type}"

class Automobile(Vehicle):
    def __init__(self, v_type, year, make, model, doors, roof):
        super().__init__(v_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def __str__(self):
        return f"Vehicle Type: {self.v_type}\nYear: {self.year}\nMake: {self.make}\nModel: {self.model}\nNumber of Doors: {self.doors}\nType of Roof: {self.roof}"

# A list of all the questions that will be asked to the user
input_list = ["What type of vehicle is being registered?\n", "What year is the vehicle?\n", "What is the make?\n", "What is the Model?\n", "How many doors does it have?\n", "What type of roof does it have? Hard Top/Rag Top/Sun Roof/Standar\n"]

for i in range(6):
    u_input = input(input_list[i])
    input_list[i] = u_input

new_vehicle = Automobile(input_list[0],input_list[1],input_list[2],input_list[3],input_list[4],input_list[5])
print("\n" * 3)
print(new_vehicle.make + "_" + new_vehicle.model)
print(new_vehicle)
