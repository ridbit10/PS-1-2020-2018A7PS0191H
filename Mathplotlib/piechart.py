from matplotlib import pyplot as plt 
x=['Advait','Ridhiman','Rishabh','Sarthak','Shiv/Shankar']
y=[100,40,60,120,70]
fig=plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
ax.pie(y, labels = x,autopct='%1.2f%%')
plt.title("Codes written ny Students")

plt.show()
