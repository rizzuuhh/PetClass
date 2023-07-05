class Pet:
    def __init__(self):
     # Initialize data attributes
     self.__name = ""
     self.__animal_type = ""
     self.__age = 0

     # Set the name of pet
    def set_name(self, name):
     self.__name = name

     # Set the animal type of the pet
    def set_animal_type(self, animal_type):
     self.__animal_type = animal_type
    
     # Set the age of the page
    def set_age(self, age):
     self.__age = age

     # Return the pet's name
    def get_name(self):
     return self.__name

     # Return the pet's animal type
    def get_animal_type(self):
     return self.__animal_type

     # Return the pet's age
    def get_age(self):
     return self.__age

# Create a Pet object
pet = Pet()
# Prompt the user for the details of the pet
name = input("Enter the pet's name: ")
animal_type = input("Enter the pet's animal type: ")
age = input("Enter the pet's age: ")
 
# Store the entered details as object attributes
pet.set_name(name)
pet.set_animal_type(animal_type)
pet.set_age(age)

# Retrieve and display the details of the pet using accessor methods
print("Pet's name:", pet.get_name())
print("Pet's animal type:", pet.get_animal_type())
print("Pet's age:", pet.get_age())