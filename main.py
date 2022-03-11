# Junk File Organizer
# Python Project To Sort Files 
import os, shutil
from extension import EXTENSION

print("Welcome To Junk File Organizer")
print("Program By - Saurabh Kumar")
print("--OPTIONS--")
print("Enter 1 For File Type Sorting")
print("Enter 2 For File Size Sorting")
typeofsort = input("Enter Sorting Method: ")
folderpath = input('Enter Your Folder Path To Sort The Files: ')



if typeofsort=="1":
    def file_finder(folderpath,file_extensions):
        files=[]
        for file in os.listdir(folderpath):
            for extension in file_extensions:
                if file.endswith(extension):
                    files.append(file)
        return files 

    for extensions_type,extension_tuple in EXTENSION.file_extensions.items():
        folder_name=extensions_type.split('_')[0]
        folder_path=os.path.join(folderpath,folder_name)
        os.mkdir(folder_path)
        for item in (file_finder(folderpath,extension_tuple)):
            item_path=os.path.join(folderpath,item)
            item_new_path=os.path.join(folder_path,item)
            shutil.move(item_path,item_new_path)

    for extensions_type,extension_tuple in EXTENSION.new_path.items():
        folder_name=extensions_type.split('_')[0]
        folder_path=os.path.join(folderpath,folder_name)
        os.mkdir(folder_path)
        for item in (file_finder(folderpath,extension_tuple)):
            item_path=os.path.join(folderpath,item)
            item_new_path=os.path.join(folder_path,item)
            shutil.move(item_path,item_new_path)
    print("Done Sorting :)")


# To Sort According To Size

if typeofsort=="2":
    def sizecheck(folderpath):
        list_dir=os.walk(folderpath)
        for dir,filename, file in list_dir:
            for f in file:
                sizeoffile=os.stat(dir+"/"+f).st_size
                try:
                    if sizeoffile < 1024:
                        if os.path.exists(folderpath+"/Byte_Files/"):
                            shutil.move(folderpath+"/"+f, folderpath+"/Byte_Files/"+f)
                        else:
                            os.mkdir(folderpath+"/Byte_Files/")
                            shutil.move(folderpath+"/"+f, folderpath+"/Byte_Files/"+f)
                    elif sizeoffile >= 1024 and sizeoffile < 1000*1024:
                        if os.path.exists(folderpath+"/KiloBytes_Files/"):
                            shutil.move(folderpath+"/"+f, folderpath+"/KiloBytes_Files/"+f)
                        else:
                            os.mkdir(folderpath+"/KiloBytes_Files/")
                            shutil.move(folderpath+"/"+f, folderpath+"/KiloBytes_Files/"+f)
                    elif sizeoffile >= 1000*1024 and sizeoffile <= 1000*1024*1024:
                        if os.path.exists(folderpath+"/MegaBytes_Files/"):
                            shutil.move(folderpath+"/"+f, folderpath+"/MegaBytes_Files/"+f)
                        else:
                            os.mkdir(folderpath+"/MegaBytes_Files/")
                            shutil.move(folderpath+"/"+f, folderpath+"/MegaBytes_Files/"+f)
                    else:
                        if os.path.exists(folderpath+"/GigaBytes_Files/"):
                            shutil.move(folderpath+"/"+f, folderpath+"/GigaBytes_Files/"+f)
                        else:
                            os.mkdir(folderpath+"/GigaBytes_Files/")
                            shutil.move(folderpath+"/"+f, folderpath+"/GigaBytes_Files/"+f)
                except FileExistsError:
                    continue
        print("Done Sorting :)")
    sizecheck(folderpath)
                

# To Sort According To Usage - To Be Added Later

# if typeofsort=="size":
#     def usagecheck(folderpath):
#         list_dir=os.walk(folderpath)
#         for dir,filename, file in list_dir:
#             for f in file:
#                 sizeoffile=os.stat(dir+"/"+f).st_atime
#                 try:


# func_to_call = {'ext':file_finder, 'size':sizecheck }
# func_to_call = {'size':sizecheck }
# func_to_call[typeofsort]()