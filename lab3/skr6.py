

def tozero()->set: 
    list = [] 
    while True: 
        try: 
            x = float(input("Input numer(0 ends inputing): ")) 
            if x == 0: 
                break 
            list.append(x) 
        except ValueError: 
            print("NOT A NUMBER!!!") 
    uniq = set(list) 
    return uniq 

print(tozero())     
 