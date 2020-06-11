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
axs[0,0].bar(x,python)
axs[0,0].title("Python marks")
#axs[0,0].xlabel("Name")
#axs[0,0].ylabel("Python marks")
#axs[0,0].subplot(1,1,2)
axs[1,0].bar(x,c)
#axs[1,0].xlabel("Name")
#axs[1,0].ylabel("C marks")
#axs[0,0].subplot(1,1,3)

axs[0,1].bar(x,cpp)
#axs[0,1].xlabel("Name")
#axs[0,1].ylabel("c++ marks")
#axs[0,0].subplot(1,1,4)

axs[1,1].bar(x,java)
#axs[1,1].xlabel("Name")
#axs[1,1].ylabel("java marks")
#axs[0,0].subplot(1,1,5)

axs[0,2].bar(x,total)
#axs[0,2].xlabel("Name")
#axs[0,2].ylabel("Total marks")
plt.show()
