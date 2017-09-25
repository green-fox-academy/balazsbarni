#### Teacher Student
#- Create `Student` and `Teacher` classes
#- `Student`
#  - learn()
#  - question(teacher) -> calls the teachers answer method
#- `Teacher`
#  - teach(student) -> calls the students learn method
#  - answer()

class Student(object):
    def question(self, teacher):
        teacher.answer()
    
    def learn(self):
        print("IDK")



class Teacher(object):
    def teach(self, student):
        student.learn()

    def answer(self):
        print("Ans")



stud = Student()
teach = Teacher()

stud.question(teach)

teach.teach(stud)