from img_operation import *

def main():
    flag=0
    while(flag==0):
        print("Enter 1 to remove image")
        print("Enter 2 to display all image names in repository")
        print("Enter 3 to display image by name")
        print("Enter 4 to rotate image")
        print("Anything else to terminate program")
        choice=int(input("Enter choice--> "))
        if(choice==1):
            path=input("Enter path of image ")
            remove(path)
        elif(choice==2):
            path=input("Enter path of repository ")
            image_names(path)
        elif(choice==3):
            path=input("Enter path of image ")
            display_image(path)
        elif(choice==4):
            path=input("Enter path of image ")
            deg=int(input("Degrees to be rotated in anticlockwise direction "))
            display_check=int(input("Enter 1 if u want to  dislply image,else anything else"))
            save_check=int(input("Enter 1 if u want to  dislply image,else anything else"))            
            save_path="None"
            if(save_check==1):
                save_path=input("Enter path to save image ")
            
            rotate_image(path,deg,display_check,save_check,save_path)
        else:
            flag=1
    print("Program terminated")

if __name__=="__main__": 
    main() 


