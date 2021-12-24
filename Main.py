import pathlib as p
import os

# Creating a Loop
z = 1
while z == 1:
    print('\nWhich Program do you want to execute? \n Enter 1 for File Organising \n Enter 2 for Folder Creating ')

    # Taking input
    inputprogram = int(input())

    # It user chooses 1st Program
    if inputprogram == 1:

        Path = ""
        files = None
        ext = set()

        # Function to get the extension file.
        def GetExtensions():
            for i in files:
                ext.add(i.suffix.replace(".", ""))

        # Function to create the respective extension folder.
        def CreateFolder():
            for i in ext:
                try:
                    os.mkdir(str(Path / i))
                except:
                    pass

        # Function to move all the files to the respective folder.
        def MoveFiles():
            for i in files:
                if i.is_file():
                    print(Path / i.suffix.replace(".", "") / i.name)
                    os.rename(str(i), Path / i.suffix.replace(".", "") / i.name)

        def main():
            global files, Path

            Path = p.Path(input("Enter Path: "))

            files = list(Path.glob("*"))

            GetExtensions()
            CreateFolder()
            MoveFiles()


        if __name__ == "__main__":
            main()

    # If user chooses 2nd Program
    elif inputprogram == 2:

        Path = p.Path(input("Enter Path: "))

        # Number of file to be created
        nof = int(input('Enter the number of files to be created : '))

        for i in range(0, nof):
            os.chdir(Path)
            NewFolder = str(input('Name the File ' + str(i + 1) + ' : '))
            os.makedirs(NewFolder)

    else:
        print('Invalid Input')

    print ('\nYour Program has been executed \n')
