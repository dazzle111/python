import os
dir = raw_input('input the dir:\n')
#filenames = os.listdir(os.getcwd())
filenames = os.listdir(dir)
for name in filenames:
	filenames[filenames.index(name)] = name
out = open('name.txt','w')
for name in filenames:
	out.write(name+'\n')
out.close()
