from zipfile import ZipFile
file_name="ball.zip"
with ZipFile(file_name,'r') as zip:
    zip.printdir()
    
