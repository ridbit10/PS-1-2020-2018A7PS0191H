from PIL import Image
import numpy as np
import os

def remove(path):
    try:
        os.remove(path)
    except FileNotFoundError:
        print("file not found")
    except:
        print ((sys.exc_info()[0]),"occured")
    else:
        print("image deleted")

def image_names(directory):
    try:
        file_paths=[]
        for root,directories,files in os.walk(directory):
            for filename in files:
                filepath=os.path.join(root,filename)
                file_paths.append(filepath)

        print("files are")
        for file in file_paths:
            print(file)
    except FileNotFoundError:
        print("file not found")
    except:
        print ((sys.exc_info()[0]),"occured")
    else:
        print("image names displayed")

def display_image(path):
    try:
        im=Image.open(path)
        im.show()
    except FileNotFoundError:
        print("file not found")
    except:
        print ((sys.exc_info()[0]),"occured")
    else:
        print("image displayed")

def rotate_image(path,degrees,display_check,save_check,save_path):
    try:
        im=Image.open(path)
        im=im.rotate(degrees)
        if(display_check==1):
            im.show()
        if(save_check==1):
            im.save(save_path)
    except FileNotFoundError:
        print("file not found")
    except:
        print ((sys.exc_info()[0]),"occured")
    else:
        print("image rotated")





