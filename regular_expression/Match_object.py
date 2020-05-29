import re
txt="It is raining in Spain"
x=re.search("in",txt)
print(x.span())
print(x.string)
print(x.group())
