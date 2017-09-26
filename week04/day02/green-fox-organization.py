class Person():
    def __init__(self, name="Jane Doe", age=30, gender="female"):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print("Hi, I\'m {}, a {} year old {}.".format(self.name, self.age, self.gender))
    
    def get_goal(self):
        print("My goal is: Live for the moment!")
        

class Student(Person):
    def __init__(self, previous_organization, skipped_days):
        pass
    
    def get_goal():
        pass
    
    def introduce():
        pass
    
    def skip_days():
        pass

class Mentor(Person):
    def __init__(self, level):
        pass
    
    def get_goal():
        pass
    
    def introduce():
        pass

class Sponsor(Person):
    def __init__(self, company, hired_students):
        pass
    
    def introduce():
        pass
    
    def hire():
        pass
    
    def get_goal():
        pass

class Pallida():
    def __init__(self, class_name, students, mentors):
        pass
    
    def add_student():
        pass
    
    def add_mentor():
        pass
    
    def info():
        pass
    

csabi = Person("csabszi", 22, "male")
csabi.introduce()
csabi.get_goal()