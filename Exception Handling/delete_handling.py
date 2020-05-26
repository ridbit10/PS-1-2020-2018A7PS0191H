import sys

Dct ={"messi":10,"suarez":9}
try:
    del Dct["iniesta"]
except:
    print ((sys.exc_info()[0]),"occured")
    print("Enter correct key")
    pass  
