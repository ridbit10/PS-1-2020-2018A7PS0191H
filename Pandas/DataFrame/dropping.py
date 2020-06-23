import pandas as pd 
player={"name":["messi","suarez","alba","ter stegen"],
        "country":["argentina","uruguay","spain","germany"],
        "jersey":["10","9","18","1"]
        }
temp={"name":["arthur"],"country":["brazil"],"jersey":["8"]}
plrs=pd.DataFrame(player)
tmp=pd.DataFrame(temp)
plrs=plrs.append(tmp)#adding gives some indexing error
plrs=plrs.drop(0)
print(plrs)
