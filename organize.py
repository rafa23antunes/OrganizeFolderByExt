import os
import glob


files_list = glob.glob("*")
extensions_set = set()

for file in files_list:
    # I had to use rsplit() instead of split() to avoid some errors. 
    # For example, with split(), a file named "hello.world.txt" would origin a folder (world_files)
    extension = file.rsplit(sep=".", maxsplit=1)
    try:
        extensions_set.add(extension[1])
    except IndexError:
        continue

# I wanto to remove "py" extension to keep my file in the folder
extensions_set.remove("py")
# Also, if I have some app in this folder, I don't want to move it
extensions_set.remove("app")



def create_Dirs():
    for dir in extensions_set:
        try:
            os.makedirs(dir+"_files")
        except FileExistsError:
            continue



def organize():
    for file in files_list:
        file_extension = file.split(sep=".")
        try:
            os.rename(file,file_extension[1]+"_files/"+file)
        except (OSError, IndexError):
            continue

create_Dirs()
organize()


