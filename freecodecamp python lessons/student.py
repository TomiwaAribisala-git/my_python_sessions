class Student: 
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name 
        self.major = major 
        self.gpa = gpa 
        self.is_on_probation = is_on_probation

    def is_on_honor_roll(self):
        if self.gpa >= 3.5: 
            return True 
        else: 
            return False

student1 = Student('jim', 'business', '5.0', True)
student1.is_on_honor_roll

class StudentCriteria(Student): 
    def student_probation_status(self):
        if self.is_on_probation == True: 
            print(f"Hi {self.name}, you are currently on probation!")
        else: 
            print(f"Hi {self.name}, you are not on probation!")

student2 = StudentCriteria('pam', 'maths', '4.5', False)
student2.student_probation_status 

