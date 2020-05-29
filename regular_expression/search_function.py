import re
txt="messi is the best"
x=re.search("^messi.*best$",txt)#starts with ends with
print(x)
txt="lionel messi is the best"
x=re.search("^messi.*best$",txt)
print(x)
x=re.search("^lionel",txt)
print(x)
