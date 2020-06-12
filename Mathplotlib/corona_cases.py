from matplotlib import pyplot as plt 
x=['1 MAR','15 MAR','30 MAR','15 APR','30 APR','15 MAY','30 MAY']
y=[1,100,1800,10000,25000,53000,90000]

plt.title("Corono cases in India")
plt.xlabel("Date ")
plt.ylabel("People")

plt.plot(x,y,'b--')
y=[0,2,32,420,1150,2750,5185]

plt.plot(x,y,'r-')
plt.show()
