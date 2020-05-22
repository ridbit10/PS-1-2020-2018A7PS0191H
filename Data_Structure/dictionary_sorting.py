player ={}
player[10]="messi"
player[20]="roberto"
player[1]="ter stegen"
player[5]="busquets"
for i in sorted (player.keys()): # sorting with respect to key
    print(i,player[i])
for i in sorted (player): #sorting with respect to value
    print(i,player[i])
