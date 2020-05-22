record ={
    "messi" : 10,
    "suarez" : 9,
    "iniesta" : 8
}

for(name,number) in  record.items():
    print("%s jersey no. is %d" %(name,number))

del record["iniesta"]
print(record)
