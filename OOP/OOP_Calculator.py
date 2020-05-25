class Calculator:
    def __init__(self , num1 , num2):
        self.num1=num1
        self.num2=num2

    def sum(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    def mul(self):
            return self.num1*self.num2
    def div(self):
            return self.num1/self.num2

s=input()
(n1,n2)=s.split()
obj = Calculator(int(n1),int(n2))
print(obj.sum())
print(obj.sub())
print(obj.mul())
print(obj.div())
