
class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        marital_status = "Married" if self.is_married else "Single"
        print(f"Name: {self.fullname}, Age: {self.age}, Marital Status: {marital_status}")


class Teacher(Person):
    salary = 0  

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        
        bonus = (self.experience // 3) * 3000
        return Teacher.salary + bonus

    def introduce_myself(self):
        super().introduce_myself()
        print(f"Experience: {self.experience} years")
        print(f"Salary: {self.calculate_salary()}")


teacher = Teacher(fullname="Сыймык Абдыракыров", age=30, is_married=True, experience=9)


Teacher.salary = 20000


teacher.introduce_myself()
