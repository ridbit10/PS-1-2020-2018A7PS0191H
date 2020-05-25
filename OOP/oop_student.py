class Student():
    
    def __init__ (self,name,age):
        self.name=name
        self.age=age
    
    def basic_info(self):
            print("my name if{},age is{}".format(self.name,self.age))

class School_Student(Student):
    
    def subject(self):
        print ("{} studies Maths,Science,English,Hindi".format({self.name}))
    
    percentage =0
    
    def grade(self):
        grade_list =["A+","A","B","C","D","E","F","G","H"]
        p = (10 - int((self.percentage/10)))
        if(self.percentage>=40):
            print("{} grade is {}".format(self.name,grade_list[p]))
        else:
            print("Fail")

class College_Student(Student):
    branch ="nil"
    marks=0;
    def subject(self):
        print("{} studies subjects related to {}".format(self.name,self.branch))
    
class Subject():
    
    def __init__(self,name,teacher,average):
        self.name=name
        self.teacher=teacher
        self.average=average

def Grade_College(name,subject,marks,average):
    grade_list1=["A","A-","B","B-","C","C-","D","F"]
    if(marks>= average +30):
        print("grade of {} in subject {} is".format(name,subject,grade_list1[0]))
    else:
        p = int((marks-average)/10)
        p = (1-(p-2))
        #print(p)
        print("grade of {} in subject {} is {}".format(name,subject,grade_list1[p]))

class Teacher:
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject

College_Student1=College_Student("Ridhiman",20)
College_Student1.branch="CS"
College_Student1.subject()

School_Student2=School_Student("Agrawal",20)
School_Student2.percentage = 30
School_Student2.grade()

Subject3 = Subject("Python","teacher",50)

College_Student1.marks=65
Grade_College(College_Student1.name,Subject3.name,College_Student1.marks,Subject3.average)
Teacher1=Teacher("Mr. Srinivasan",Subject3)
print("{} teaches subject {}".format(Teacher1.name,Teacher1.subject.name))
