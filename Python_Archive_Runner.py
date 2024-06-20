import zipfile
import os

os.system("cls")

print("Python Archive Runner | Version 0.4")
print("mac and linux versions coming eventualy")
print("\ncommands: \nexit - exits the program \ndir - prints current directory \nrun - runs PAR of your choice \nabout - prints about screen \nclear - resets the screen \nconvert - converts .zip files to .par files\n")

list = []

while True:
    cmd = input()
    if cmd == "exit":
        os.system("cls")
        exit()
    elif cmd == "dir":
        dir = os.listdir()
        print("\n", dir, "\n")
    elif cmd == "about":
        print("\nPython_Archive_Runner \nversion 0.4\nmade for windows\nmade by wizard studios\nCopyleft MMXXIV - MMXXV (remind me to update)\n")
    elif cmd == "clear":
        os.system("cls")
        print("Python Archive Runner | Version 0.4")
        print("mac and linux versions coming eventualy")
        print("\ncommands: \nexit - exits the program \ndir - prints current directory \nrun - runs PAR of your choice \nabout - prints about screen \nclear - resets the screen \nconvert - converts .zip files to .par files \n")
    elif cmd == "convert":
        print("\ntype the name of the file you want to convert to .par (extension required)\n")
        sfile = input()
        if os.path.isfile(sfile):
            print("\ntype the what you want the name of the output file to be (no extension required)\n")
            ofile = input()    
            os.rename(sfile, ofile + ".par")
        else:
            print("Mission Failed, we'll get em' next time: you miswrote the filename")
    elif cmd == "run":
        print("\ntype the name of the .par file that you want to run or type exit to exit (include the extension)\n")
        file = input()

        if os.path.isfile(file):
            with zipfile.ZipFile(file, "r") as read:
                read.extractall()
                for i in read.namelist():
                    list.append(i)
                read.close()

            with zipfile.ZipFile(file, "w") as read:
                os.system("python main.py")
                for i in list:
                    read.write(i)
                    os.remove(i)
                read.close()
        else:
            print("Mission Failed, we'll get em' next time: you miswrote the filename")