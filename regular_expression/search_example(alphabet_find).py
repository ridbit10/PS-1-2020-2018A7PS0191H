import re
dict ={"messi","neymar","suarez","aguero","iniesta","dybala"}
for player in dict:
    x=re.findall("[s]",player)
    if x:
        print(player)
