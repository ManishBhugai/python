import os

files=os.listdir()
for file in files:
    if os.path.isfile(file):
        if os.path.getsize(file)==0:
            os.remove(file)