import unicodedata
import io

name = input("What actor would you like to see? \n To quit press q")
if name == "q" or "Q": # check if user wants to quit script
    import sys
    sys.exit(0)

for files in "C:\Users\omega\Documents\Training\Lorine Python\IndexMe": #to go through all files in folder
    if name == files.decode("utf-8"): # if found actor nam efrom user index
        with open(f'{name}.txt', 'w') as f: # write into new file using the name of the actor
            f.write(files)