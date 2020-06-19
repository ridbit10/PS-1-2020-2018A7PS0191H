from branch import *
from course import *

class Student:
    def __init__(self,name,id,age,current_sem,sex,branch):
        self.name=name
        self.id=id
        self.age=age
        self.current_sem=current_sem
        self.branch=branch
        self.sex=sex
    def get_current_courses(self):
        current_courses=[]
        print(self.current_sem)
        for x in self.branch.courses:
            if (x.sem == self.current_sem):
                print(x.name)
                current_courses.insert(len(current_courses),x)

        return current_courses
    def form_students(self):
        

#c=form_branch("CS","A7")
#for x in c:
#    print(x.name)
CS=Branch("CS","A7",form_branch("CS","A7"))
Raj=Student("Raj","shbc","23","1","M",CS)
crs=Raj.get_current_courses()
for x in crs:
    print(x.name)

