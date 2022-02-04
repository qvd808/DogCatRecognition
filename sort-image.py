import os, shutil
## Copy the image in train and sort it into the new folder


path = "./dogs-vs-cats/train"

## Since we know the first character of the file name is either d for dog or c for cat, we can only need to check the first character
dogs = [path + '/' + d for d in os.listdir(path) if d[0] == 'd']
cats = [path + '/' + c for c in os.listdir(path) if c[0] == 'c']

if (not os.path.exists("./sort-folder")):
    os.mkdir("./sort-folder")
    os.mkdir("./sort-folder/cats")
    os.mkdir("./sort-folder/dogs")

for d in dogs:
    shutil.copy(d, "./sort-folder/dogs")

print("Finished copied dogs")

for c in cats:
    shutil.copy(c, "./sort-folder/cats")

print("Finished copied cats")
