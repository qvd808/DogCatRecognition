import matplotlib.pyplot as plt

X1 = [1,2,3,4,5]
Y1 =  [2,4,6,8,10]

plt.plot(X1, Y1, label = "plot 1")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Testing")
plt.legend()

plt.savefig('./sort-folder/testing.jpg', bbox_inches = "tight", dpi = 150)
plt.show()

import datetime
x = datetime.datetime.now()
with open('./sort-folder/Report.txt', 'w') as f:
    f.write(str(x) + '\n')
    f.write(str(x))

import shutil,os

shutil.copy(os.path.basename(__file__), "./sort-folder")