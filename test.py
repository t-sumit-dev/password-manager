class Teacher:
    def __init__(self,name):
        self.name = name
class School:
    def __init__(self,teacher):
        self.teacher = teacher
    def show(self):
        print("TEACHER : ",self.teacher.name)
teacher1 = Teacher("SKS")
school = School(teacher1)
school.show()
a= 10
b= 20
print(a+b)
