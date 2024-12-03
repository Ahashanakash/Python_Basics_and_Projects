from person import Person
from school import School

class Student(Person):
    def __init__(self, name, classroom) -> None:
        super().__init__(name)
        self.classroom = classroom
        self.__id = None
        self.marks = {}
        self.subject_grade = {}
        self.grade = None 
    
    def calculate_final_grade(self):
        sum = 0
        for grade in self.subject_grade.values():
            point = School.grade_to_value(grade)
            sum += point
        if sum == 0:
            gpa = 0.00
            self.grade = 'F'
        else:
            gpa = round(sum / len(self.subject_grade),2)
            self.grade = School.value_to_grade(gpa)
        return f"{self.name} Final Grade : {self.grade} with GPA = {gpa}"
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value):
        self.__id = value