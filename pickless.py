import pickle

a = ['test value','test value 2','test value 3']

file_Name = "testfile"
# open the file for writing
fileObject = open(file_Name,'wb')

# this writes the object a to the
# file named 'testfile'
pickle.dump(a,fileObject)

# here we close the fileObject
fileObject.close()
# we open the file for reading
fileObject = open(file_Name,'rb')
# load the object from the file into var b
b = pickle.load(fileObject)
print (b)
#b
#['test value','test value 2','test value 3']
#a==b
#True
