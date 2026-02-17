from asyncio.log import logger
import logging
logging.basicConfig(level=logging.INFO)

class User:
    def __init__(self, username, **kwargs):
        self.username = username
        self.details = kwargs

    def display(self):
        print(f"Username: {self.username}")
        for key, value in self.details.items():
            print(f"{key.capitalize()}: {value}")

user1 = User("john_doe", email="sagar12@gmail.com", phone="1234567890", address="Pune")
user1.display()

class User:
    def __init__(self, username, **kwargs):
        self.username = username
        self.details = kwargs
    
    def display(self):
        print(f"Username : {self.username}")
        for key, value in self.details.items():
            print(f"{key.capitalize()}: {value}")

user2 = User("alice", email="rama@gamil.com", phone="9876543210")
user2.display()


class Labour:
    """A class to represent a Labour with optional wage."""
    total_labour = 0 # class variable to keep track of total labour instances
    def __init__(self, name, surname, wage=None):
        self.name = name # instance variable for name
        self.surname = surname # instance variable for surname
        self.wage = wage # instance variable for wage
        Labour.total_labour += 1

    def display(self):
        print(f"Labour Name: {self.name} {self.surname}, Wage: {self.wage}")

    @classmethod
    def get_total_labour(cls):
        return Labour.total_labour
    @staticmethod
    def is_valid_wage(wage):
        if wage <=2000:
            logging.info("Wage is valid")
        else:
            logging.error("Wage is not valid")


manish = Labour("mnish", "kumar", 1000)
ramesh = Labour("ramesh", "kumar", 2000)
sona = Labour("sona", "kumar", 3000)
nana = Labour("nana", "kumar", 4000)
print(f"Total Labour: {Labour.get_total_labour()}")
print(Labour.is_valid_wage(3000))
# manish.display()
# ramesh.display()

# Inheritance Example
# Inheritance allows a class to inherit attributes and methods from another class
# This promotes code reuse and establishes a relationship between classes.
# In this example, we will create a base class `Person` and a derived class `Student` that inherits from `Person`.
# The `Student` class will inherit the properties and methods of the `Person` class.
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.age = age
        self.surname = surname
        self.email = self.name + "." + self.surname + "@gamil.com"


    def display(self):
        print(f"Name: {self.name} {self.surname}, Age: {self.age}, Email: {self.email}")

class Student(Person):
    pass

lab = Student("Lab", "shem", 20)
lab.display()