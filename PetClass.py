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
# Store the entered details as object attributes
# Retrieve and display the details of the pet using accessor methods