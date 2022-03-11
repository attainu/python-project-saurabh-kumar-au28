# Python-Project
## **Junk File Organizer**
### `SAURABH KUMAR`

### **Aim**

The aim of this project is to build a python program that runs as a command-line tool. Basically, as a lazy programmer, my desktop is full of files as shown below. Due to a large number of files, it is a daunting task to sit and organize each file. To make that task easy, we need a Python script that comes in handy and returns a folder where all the files are organized in a well-manner within seconds. It should organize by size, last used or even extensions.

### **Approach**

By using the os module of python to recursively list out all the files that are present in the folders with their relative and absolute path then create a new folder with the parent called organized which will contain all the files in organized sub-folders.

And for size we use the os module of python and os.stat() method to retrive and read the size using "st_size" then using the if else statement inside a try expect and a for loop. Then sorting the files asccording to the size and putting them to their respective Folders according to the size of file.

### **Steps**

We import os and shutil at first.

     The OS module in python provides functions for interacting with the operating system. OS, comes under Python’s standard utility modules. This module provides a portable way of using operating system dependent functionality. The *os* and *os.path* modules include many functions to interact with the file system.

     Shutil module in Python provides many functions of high-level operations on files and collections of files. It comes under Python’s standard utility modules. This module helps in automating the process of copying and removal of files and directories. (Ex - shutil.move() method Recursively moves a file or directory (source) to another location (destination) and returns the destination.)

`For the File Type Sort`

We create the dictionaries for the folders. And the code will have the defined directories for each type of extentions 
     
     (Example - 'Audio':('.mp3','.wav','.flac', '.m4a', '.aac') Here we define the type of extentions of files for the sub-folder Audio)

Then we start mapping the file formats with directory. By creating a function and moving them according to the extention list in the dictionary. It will also check if there is any existing directory as defined by us in the program, if any existing folder is there it contines or else it creates a new directory. And then all the files will be categorized according to their extension to the appropriate folder as defined.

`For The Size Sorting of Files`

For size we use the os module of python and os.stat() method to retrive and read the size using "st_size" then using the if else statement inside a try expect and a for loop. Then sorting the files asccording to the size and putting them to their respective Folders according to the size of file.

Here we create a function to get the file size and sorting the files according to their respective file sizes.
  
     Here we are sorting the files into 4 Differnt Folders According To Size that are - "Byte_Files" for files under 1024 Bytes, "KiloByte_Files", "MegaByte_Files" and "GigaByte_Files".



## **How This Program Runs**

So this code basically runs as any normal python .py code.
It Shows the user Options of sorting.

Then, it asks for the method i.e 
Enter 1 For File Type Sorting 
And Enter 2 For File Size Sorting.

Then it asks for user input for the path of the folder where the sorting is to be done.


#### `More Features That Are To Be Added`

Sorting Accoding To File Usage, Creation Date/Time.