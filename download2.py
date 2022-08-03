from distutils import extension
import os
import shutil
from_dir= 'C:/Users/User/Downloads'
to_dir='C:/Users/User/Desktop/python'
list_Of_Files = os.listdir(from_dir)
#print(list_Of_Files)
for File_Name in list_Of_Files:
    name,extension= os.path.splitext(File_Name)
#    print(name)
#   print(extension)
    if extension=='':
        continue
    if extension in ['.pdf']:
        path1=from_dir+'/'+ File_Name
        path2=to_dir+'/' + "image_Files"
        path3=to_dir+'/' + "image_Files" + File_Name
        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving")
            shutil.move(path1,path3)