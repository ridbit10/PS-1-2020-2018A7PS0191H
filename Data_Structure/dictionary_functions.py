dict = {'Name': 'Ridhiman', 'Age': 20, 'College' : "Bits-HYD",
 'Branch' : 'CS' }
print("length is {}".format(len(dict)))
dict.clear()
print("length is {}".format(len(dict)))

dict_1={'Name':'Messi','Age':33 ,'Club':'FC Barcelona'}
dict_2=dict_1.copy()
print("New dictionary -->",dict_2)

#key doesnt exist so add new values
dict_2.update({'Country':'Argetina'})
print(" dictionary -->",dict_2)

#key exists so updates it
dict_2.update({'Age':32})
print(" dictionary -->",dict_2)

del dict_2['Age']
print(" dictionary -->",dict_2)

seq =('Name','Age','Club')
dict_3=dict.fromkeys(seq,10)#keys of seq and all have values
print(" dictionary -->",dict_3)

# to-do print("New dictionary -->".format(str(dict_3)))


