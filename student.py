class Student:
    def __init__(self,name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        print(f"Name {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grade}")

    def is_passing(self):
        if self.grade > 60:
            print(f"{self.name} is passing")
        else:
            print(f"{self.name} is not failing")

student = Student("Vadim",43,83)

student.introduce()
student.is_passing()
