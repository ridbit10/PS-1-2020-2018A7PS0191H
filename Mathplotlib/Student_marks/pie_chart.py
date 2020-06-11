from matplotlib import pyplot as plt 
import numpy as np
x=['Adv','Rid','Ris','Sar','Shiv']
python=[60,50,70,75,55]
c=[34,76,12,65,43]
cpp=[54,100,34,89,90]
java=[45,78,90,23,54]
total=[0,0,0,0,0]
for i in range(0,5,1):
    total[i]=python[i]+c[i]+cpp[i]+java[i]
fig,axs = plt.subplots(2,3)
#plt.subplot(1,1,1)
subject=['python','c','c++','java']
c1=0
x=[python[c1],c[c1],cpp[c1],java[c1]]
c1=c1+1
axs[0,0].pie(x, labels = subject,autopct='%1.2f%%')
axs[0,0].set_title("Advait marks")
#axs[0,0].xlabel("Name")
#axs[0,0].ylabel("Python marks")
#axs[0,0].subplot(1,1,2)
x=[python[c1],c[c1],cpp[c1],java[c1]]
c1=c1+1
axs[1,0].pie(x, labels = subject,autopct='%1.2f%%')
axs[1,0].set_title("Ridhiman marks")
#axs[1,0].xlabel("Name")
#axs[1,0].ylabel("C marks")
#axs[0,0].subplot(1,1,3)
x=[python[c1],c[c1],cpp[c1],java[c1]]
c1=c1+1
axs[0,1].pie(x, labels = subject,autopct='%1.2f%%')
axs[0,1].set_title("Rishabh marks")
#axs[0,1].xlabel("Name")
#axs[0,1].ylabel("c++ marks")
#axs[0,0].subplot(1,1,4)
x=[python[c1],c[c1],cpp[c1],java[c1]]
c1=c1+1
axs[1,1].pie(x, labels = subject,autopct='%1.2f%%')
axs[1,1].set_title("Sarthak marks")
#axs[1,1].xlabel("Name")
#axs[1,1].ylabel("java marks")
#axs[0,0].subplot(1,1,5)
x=[python[c1],c[c1],cpp[c1],java[c1]]
c1=c1+1
axs[0,2].pie(x, labels = subject,autopct='%1.2f%%')
axs[0,2].set_title("Shiv/Shankar marks")
#axs[0,2].xlabel("Name")
#axs[0,2].ylabel("Total marks")
plt.show()
