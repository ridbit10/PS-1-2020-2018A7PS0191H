import sys

Lst =['a',0,2,3]
for i in Lst:
    r=0
    try:
        print("Entry is ",i)
        r=(1/int(i))
        print("reciprocal is",r)
        print()
        pass
    except:
        print ((sys.exc_info()[0]),"occured")
        print()
        pass
