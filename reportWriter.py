import datetime, os


# target_size = (150,150)
# batch_size = 32
# train_size = len(next(os.walk("./sort-folder/cats"))[2]) + len(next(os.walk("./sort-folder/dogs"))[2])
# test_size = len(next(os.walk("./cats_and_dogs_filtered/validation/cats"))
#                 [2]) + len(next(os.walk("./cats_and_dogs_filtered/validation/dogs"))[2])
# path = "./sort-folder"

def Writer(train_size, test_size, batch_size, target_size, path):
    x = datetime.datetime.now()
    with open(path + str('/Report.txt'), 'w') as f:
        f.write(str(x) + '\n')
        f.write(str(train_size) + '\n')
        f.write(str(test_size) + '\n')
        f.write(str(batch_size) + '\n')
        f.write(str(target_size))

# Writer(train_size, test_size, batch_size, target_size, path)
