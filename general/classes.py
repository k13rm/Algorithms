

age = 12
name = 'John'
surname = 'Doe'

class Student:
    def __init__(self, age, name, surname):
        self.age = age
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}, Age: {self.age}"
    
class School:
    def __init__(self, student):
        self.student = student
    
kerem = Student(13, "Kerem", "Duruk")
nazir = Student(26, "Nazir", "Nayal")

print(kerem)
print(nazir)