import shutil, os
nameplace = "test"
filename = "test.csv"
name = nameplace + filename
if os.path.exists(name) and os.path.isfile(name):
    os.remove(name)
    shutil.copyfile(filename, name)
else:
    shutil.copyfile(filename, name)


import logging

data = []
clean_data = []
filtered_data = []

with open("test.csv", "r") as f:
    data = f.readlines()
    print(data)
    for x in data:
        print(x.strip())
        val = x.strip()
        clean_data.append(val)
        clean_data_l = list(filter(''.__ne__, clean_data))
    print(clean_data_l)
    