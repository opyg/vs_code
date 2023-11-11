#!C:\Users\rety1\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe

def uniq(list1,list2)->list: 
    uniqone = [x for x in list1 if x not in list2]
    return uniqone

a = [1,4,2,6,3]
b = [8,5,3,4,2]
print(uniq({'523','3525'},{3,52,62}))
