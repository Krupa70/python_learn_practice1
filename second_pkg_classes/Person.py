class Person:
    species = "Human" # class level constructor
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Person details: name = {self.name}, age = {self.age }")

    #class level variables are accessed inside class methods using cls
    @classmethod
    def display_species_info(cls):
        print(f"Species: {cls.species}")

    @staticmethod
    def general_info(book):
        print(f"""Book name: {book}. Humans are bipedal primates \
              belonging to the species.""")

# Run the code 
person = Person("Alice", "25")
person.display_info()
Person.display_species_info()   
Person.general_info