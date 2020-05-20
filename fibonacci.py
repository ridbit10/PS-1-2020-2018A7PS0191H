f1=0 
f2=1
n = int(input())
if(n>=1):
    print(f1)
if(n>=2):
    print(f2)
for x in range (1,n-1):
    print(f1+f2)
    c=f1+f2
    f1=f2
    f2=c
