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
    def __init__(self, name, age, gender, previous_organization="The School of Life", skipped_days=0):
        super().__init__(name, age, gender)
        self.previous_organization = previous_organization
        self.skipped_days = skipped_days
        
    def get_goal(self):
        print("Be a junior software developer.")
    
    def introduce(self):
        print("Hi, I\'m {}, a {} year old {} from {} who skipped {} days from the course already.".format(self.name, self.age, self.gender, self.previous_organization, self.skipped_days))
    
    def skip_days(self, number_of_days):
        self.skipped_days += number_of_days
        

class Mentor(Person):
    def __init__(self, name, age, gender, level="Intermediate"):
        super().__init__(name, age, gender)
        self.level = level
    
    def get_goal(self):
        print("Educate brilliant junior software developers.")
    
    def introduce(self):
        print("Hi, I\'m {}, a {} year old {} {} mentor.".format(self.name, self.age, self.gender, self.level))

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
    

csabi = Mentor("csabszi", 22, "male")
csabi.introduce()
csabi.get_goal()