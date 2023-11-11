def division(a:float,b:float)->float:
    return a/b

def uniq(list1,list2)->list: 
    uniqone = [x for x in list1 if x not in list2]
    return uniqone

def nonpair(list)->list:
    l = [x for x in list if x%2 != 0]
    return l
a = [1,4,2,6,3]
b = [8,5,3,4,2]



