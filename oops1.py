class Employee:
    def __init__(self):
        print("strated executing attributes or data")
        self.id=123
        self.salary=20000
        self.desig="SDE"
        print("data has been initiated")
#creating an object of the class


    def travel(self,dest):
        print("this travel method is called manually")
        print(f"Employee is now travelling to {dest}")

sam=Employee()
sam.travel("paris")

#print(sam.id)
print(type(sam))