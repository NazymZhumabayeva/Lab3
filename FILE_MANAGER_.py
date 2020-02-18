import os

from os import path

import os.path

def FILES():
    
    print("""
    1 - delete file
    
    2 - rename file
    
    3 - add content to this file
    
    4 - rewrite content of this file
    
    5 - return to the parent directory
    """)

def DIRECTORIES():
    print("""
    1 - rename directory

    2 - print number of directories in it
    
    3 - print number of files in it
    
    4 - list content pf the directory
    
    5 - add file to this directory
    
    6 - add new directory to this directory
    """)

def MAINMENU():
    print("""WELCOME TO FILE MANAGER! WHAT DO YOU WANT TO WORK WITH?
        1 - Files
        2 - Directories
        3 - Exit
    """)

while True:
    MAINMENU()
    what = int(input())
    if what == 1:
        FILES()
        choice = int(input())
    #DELETING FILE
        if choice == 1:
            print('Enter a name of the file you need to delete:')
            file_name = input()
            if os.path.exists(file_name):
                os.remove(file_name)
                print("File was removed successfully!")
                continue
            else:
                print(f"Error: there does not exist {file_name} in current directory")
                continue
    #RENAMING A FILE
        elif choice == 2:
            print('Enter the name of file')
            file_name = str(input())
            print("Enter a new name:")
            new_name = str(input())
            os.rename(file_name, new_name)
            print("File was renamed successfull!")
            continue
    #ADDING A CONTENT A FILE
        elif choice == 3:
            print('Enter the name of file to add content:')
            file_name = input()
            if os.path.exists(file_name):
                file_new = open(file_name, 'a')
                add = str(input("Enter what you want to add: "))
                file_new.write(add)
                file_new.close()
                print("New contect was added to file successfull!")
                continue
            else:
                print("The file does not exist in this directory.")
                continue
    #REWRITNIG A FILE
        elif choice == 4:
            print('What file you want to rewrite?: ')
            file_name = input()
            if os.path.exists(file_name):
                file_new = open(file_name, 'w')
                rewrite = input("What do you want to rewrite?: ")
                file_new.write(rewrite)
                file_new.close()
                print("File was rewritten.")
                continue
            else:
                print(f"{file_name} does not exist in this directory.")
                continue
        elif choice == 5:
            print("Your parent directory is: ")
            print(os.path.dirname(os.getcwd()))
            continue
    elif what == 2:
        DIRECTORIES()
        choice2 = int(input())
        #RENAMIG A DIRECTORY
        if choice2 == 1:
            print('Enter the name of directory you want to rename:')
            dir_name = str(input())
            print('Name of new directory: ')
            new_name = str(input())
            os.rename(dir_name, new_name)
            print('Directory was renamed!')
            continue
        #NUMBER OF DIRECTORIES IN DIR
        elif choice2 == 2:
            dir = input('Enter the name of directory: ')
            if os.path.exists(dir):
                number = len([1 for x in list(os.scandir(dir)) if x.is_dir()])
                print('There are ' + str(number) + ' directories in your directory.')
                continue
            else:
                print('Directory does not exist.')
                continue
        #NUMBER OF FILES 
        elif choice2 == 3:
            dir = input('Enter the name of directory: ')
            if os.path.exists(dir):
                dir_list = os.listdir(dir)
                num_files = len([1 for f in list(os.scandir(dir)) if f.is_file])
                print('There are ' + str(num_files) + ' files in your directory.')
                continue
            else:
                print('Directory does not exist.')
                continue
        #LIST
        elif choice2 == 4:
            print(os.listdir())
            continue
        #NEW FILE ADDING
        elif choice2 == 5:
            file_name = input('Enter the name for new file: ')
            new_file = open(file_name, 'w')
            print('File was added to rhis directory successfully.')
            continue
        #NEW DIRECTORY
        elif choice2 == 6:
            dir_name = input('Enter the name for new directory: ')
            os.mkdir(dir_name)
            print("New directory was added successfully!")
        #EXIT
    else:
        print('OK!')
        exit()