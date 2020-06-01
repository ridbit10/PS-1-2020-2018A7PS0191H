import sys
import re
from pb_contact import Contact_Detail
from pb import *

def main():
    flag=0
    while(flag==0):
        print("Enter 1 to add contact")
        print("Enter 2 to update existing contact")
        print("Enter 3 to display existing contact")
        print("Enter 4 to delete existing contact")
        print("Enter 5 to print name with specific alphabet")
        print("Enter anything else to terminate ")
        choice = int(input("Enter choice--> "))
        if(choice==1):#add contact
            name=input("Enter name ")
            number=input("Enter number ")
            address=input("Enter address ")
            contact=Contact_Detail(name,number,address)
            add(contact)
        elif(choice==2):
            name=input("Enter name ")
            number=input("Enter number ")
            address=input("Enter address ")
            contact=Contact_Detail(name,number,address)
            update(contact)
        elif(choice==3):
            name=input("Enter name ")
            display(name)
        elif(choice==4):
            name=input("Enter name ")
            delete(name)
        elif(choice==5):
            alphabet=input("Enter alphabet ")
            specific_alphabet(alphabet)
        else:
            flag=1

    print("Program terminated!!!")           

if __name__=="__main__": 
    main()  
