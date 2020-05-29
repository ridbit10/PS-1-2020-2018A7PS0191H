import sys
import re

class Contact_Detail:
    def __init__(self,name,number,address):
        self.name=name
        self.number=number
        self.address=address


dict_phone={}
try:
     phone_book=open("phonebook.txt",'r',encoding='utf-8')
     for line in phone_book:
        #print("jscbsh")
        #print(line)
        s=list(line.split(","))
        #print(s[0])
        Detail1=Contact_Detail(s[0],s[1],s[2])
        dict_phone[Detail1.name]=Detail1
        #print(Detail1.name)
except:
    print ((sys.exc_info()[0]),"occured")
finally:
    phone_book.close()



flag=0
while(flag==0):
    print("Enter 1 to add contact")
    print("Enter 2 to update existing contact")
    print("Enter 3 to display existing contact")
    print("Enter 4 to delete existing contact")
    print("Enter 5 to print name with specific alphabet")
    print("Enter anything else to terminate ")
    choice = int(input())
    

    if(choice==1):#add contact
        name=input("Enter name ")
        number=input("Enter number ")
        address=input("Enter address ")
        Detail2=Contact_Detail(name,number,address)
        check=0
        if name in dict_phone:
            check=1
        x=re.findall("[0-9]",number)
        if len(x) is not len(number):
            check=2
        if check==0:
            try:
                phone_book=open("phonebook.txt",'a+',encoding='utf-8')
                phone_book.write("{},{},{}\n".format(name,number,address))
                dict_phone[name]=Detail2
            except:
                print ((sys.exc_info()[0]),"occured")
            else:
                print("Contact succesfully added!!!!!")
            finally:
                phone_book.close()
        elif check==2:
            print("Number is not valid")
        else:
            print("Name already exists")
            print()
    

    elif(choice==2):#update contact
        name=input("Enter name ")
        number=input("Enter number ")
        address=input("Enter address ")
        check=0
        if name in dict_phone:
            check=1
        x=re.findall("[0-9]",number)
        if len(x) is not len(number):
            check=2

        if(check==1):
            Detail1=Contact_Detail(name,number,address)
            dict_phone[name]=Detail1
            try:
                phone_book=open("phonebook.txt",'w',encoding='utf-8')
                for record in dict_phone:
                    #phone_book.write("jvhbdhf")
                    phone_book.write("{},{},{}\n".format(dict_phone[record].name,dict_phone[record].number,dict_phone[record].address))
            except:
                print ((sys.exc_info()[0]),"occured")
            else:
                print("Contact successfully updated")
            finally:
                phone_book.close()
        elif check==2:
            print("Number is not valid")
        else:
            print("Name doesnot exist") 
    

    elif(choice==3):#display contact
        name=input("Enter name ")
        check=0
        if name in dict_phone:
            check=1
        if(check==1):
            print("{},{},{}".format(dict_phone[name].name,dict_phone[name].number,dict_phone[name].address))
            print("Contact succesfully found and printed!!!")
        else:
            print("Name doesnot exist")
    

    elif(choice==4):#delete contact
        name=input("Enter name ")
        check=0
        if name in dict_phone:
            check=1
        if(check==1):
            try:
                del dict_phone[name]
                phone_book=open("phonebook.txt",'w',encoding='utf-8')
                for record in dict_phone:
                    #phone_book.write("jvhbdhf")
                    phone_book.write("{},{},{}\n".format(dict_phone[record].name,dict_phone[record].number,dict_phone[record].address))
            except:
                print ((sys.exc_info()[0]),"occured")
            else:
                print("Contact successfully deleted")
            finally:
                phone_book.close()
        else:
            print("Name doesnot exist")
    
    elif(choice==5):
        alphabet=input("Enter alphabet ")
        try:
             phone_book=open("phonebook.txt",'r',encoding='utf-8')
             for line in phone_book:
                s=list(line.split(","))
                x=re.findall(alphabet,s[0])
                if x:
                    print("{} {} {}".format(s[0],s[1],s[2]))
        except:
            print ((sys.exc_info()[0]),"occured")
        finally:
            phone_book.close()
    else:
        flag=1

print("Program terminated!!!!")
