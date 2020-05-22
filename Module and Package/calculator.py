import calculations
a,b = input().split() #input 2 no.s
ch =int(input()) # input choice for calculator
a=int(a)
b=int(b)
if(ch==1):
    print(calc.sum(a,b))
if(ch==2):
    print(calc.subtract(a,b))
if(ch==3):
    print(calc.multiply(a,b))
if(ch==4):
    print(int(calc.divide(a,b)))
