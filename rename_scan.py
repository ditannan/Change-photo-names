import os
path1 = os.path.abspath("test1/")
path2 = os.path.abspath("test2/")
path3 = os.path.abspath("test3/")

for i, f in enumerate(os.listdir(path1)):
    extension0 = os.path.splitext(f)[1]
    extension = os.path.splitext(f)[0][-8:]
    extension1 = os.path.splitext(f)[0][15:16]
    newname = "%s_%s%s" % (extension, extension1,extension0)
    os.rename(os.path.join(path1, f),os.path.join(path1, newname))
    #print(newname)
    
 for i, f in enumerate(os.listdir(path2)):
    extension0 = os.path.splitext(f)[1]
    extension = os.path.splitext(f)[0][-8:]
    extension1 = os.path.splitext(f)[0][15:17]
    newname = "%s_%s%s" % (extension, extension1,extension0)
    os.rename(os.path.join(path2, f),os.path.join(path2, newname))
    #print(newname)
    
 for i, f in enumerate(os.listdir(path3)):
    extension0 = os.path.splitext(f)[1]
    extension = os.path.splitext(f)[0][-8:]
    extension1 = os.path.splitext(f)[0][15:18]
    newname = "%s_%s%s" % (extension, extension1,extension0)
    os.rename(os.path.join(path3, f),os.path.join(path3, newname))
    #print(newname)
