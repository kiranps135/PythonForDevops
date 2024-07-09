import os
import os.path
import shutil
#os.mkdir("folder1")
#path = "folder1/demo3"
#os.open(path ,  os.O_CREAT)# create a new file
#a= os.listdir('.')
#print(a)
#x = os.path.exists('kiran.txt') #
#print(x)
#os.rmdir('folder1')
#os.remove('new.txt') # remove file
#os.removedirs('folder1')
# delete the directory recursively
shutil.rmtree('folder1')
a= os.listdir('.')
print(a)