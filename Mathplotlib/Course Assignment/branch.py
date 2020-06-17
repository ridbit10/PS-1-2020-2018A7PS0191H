from course import *

class Branch:
    def __init__(self,name,id,courses):
        self.name=name
        self.id=id
        self.courses=courses



all_courses=get_courses()

Branches=[]

def form_branch(branch_name,id):
    branch_courses=[]
    c=0
    for course in all_courses:
        if(course.branch==branch_name):
            branch_courses.insert(c,course)
            c=c+1

    if(c>0):
        temp_branch=Branch(branch_name,id,branch_courses)
        Branches.insert(len(Branches),temp_branch)

form_branch("CS","A7")

for x in Branches[0].courses:
    print (x.name)
    