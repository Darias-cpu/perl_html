class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

person1 = Person("Alice", 30, "Female")
print(person1.display_info())


