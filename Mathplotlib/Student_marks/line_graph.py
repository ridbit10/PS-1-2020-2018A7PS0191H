from matplotlib import pyplot as plt 
import numpy as np

students=['Advait','Ridhiman','Rishabh','Sarthak','Shiv']
marks=[[60,50,70,75,55],[34,36,12,65,43],[54,75,34,89,90],[45,68,90,23,54]]
subjects=['Python','C','C++','Java']
clrs=['g','r','b','k','y']

def display(i):
    individual_marks=[marks[0][i]]
    for j in range(1,4,1):
        individual_marks.insert(j,marks[j][i]+individual_marks[j-1])
    plt.plot(subjects,individual_marks,marker='o',color=clrs[i],label=students[i])  

for i in range(0,5,1):
    display(i)

plt.ylabel("Marks")
plt.xlabel("Subjects")
plt.legend(loc="upper left")
plt.title("Student ranking")

mng = plt.get_current_fig_manager()
mng.window.state('zoomed')

plt.show()
