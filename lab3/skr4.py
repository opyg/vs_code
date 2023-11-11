

def nonpair(list)->list:
    
    l = [x for x in list if x%2 != 0]

    return l

my_list = [2,4,32,2,62,36,2,6,37,74,253,16]
print(nonpair(my_list))