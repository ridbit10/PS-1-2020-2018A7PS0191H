from matplotlib import pyplot as plt 
import numpy as np

students=['Advait','Ridhiman','Rishabh','Sarthak','Shiv']
marks=[[60,50,70,75,55],[34,36,12,65,43],[54,75,34,89,90],[45,68,90,23,54]]
subjects=['Python','C','C++','Java']

fig,axs = plt.subplots(2,3)

def display(i):
    individual_marks=[]
    for j in range(0,4,1):
        individual_marks.insert(j,marks[j][i])
    axs[(i%2),int((i/2))].pie(individual_marks, labels = subjects,autopct='%1.2f%%')
    students[i]=students[i]+" marks"
    axs[(i%2),int((i/2))].set_title(students[i])    

for i in range(0,5,1):
    display(i)

fig.delaxes(axs[1][2])

mng = plt.get_current_fig_manager()
mng.window.state('zoomed')

plt.show()
