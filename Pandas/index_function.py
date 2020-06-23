import pandas as pd 
player={"name":["messi","suarez","alba","ter stegen"],
        "country":["argentina","uruguay","spain","germany"],
        "jersey":["10","9","18","1"]
        }

plrs=pd.DataFrame(player)
plrs.index=["A","B","C","D"]
print(plrs)
