import re
txt="It is raining in Spain"
x=re.sub("\s","\n",txt)#replacing blank space with lines
print(x)
