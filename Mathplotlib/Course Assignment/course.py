import sys
import re

class Course:
    def __init__(self,name,id,branch,sem,grade_value):
        self.name=name
        self.id=id
        self.branch=branch
        self.sem=sem
        self.grade_value=grade_value
    


def get_courses():
    courses=[]
    i=0
    try:
        crs=open("course.txt",'r',encoding='utf-8')    
        for line in crs:
            s=list(line.split(","))
            s[len(s)-1].strip("\n")
            #print(s)
            if(len(s)==5):
                temp_course=Course(s[0],s[1],s[2],s[3],s[4])
                courses.insert(i,temp_course)
                i=i+1
    except:
        print(i)
        print ((sys.exc_info()[0]),"occureda")
    else:
        return courses
    finally:
        crs.close()


courses=get_courses()
#print(courses[17].grade_value)