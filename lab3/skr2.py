

def ins()->None:
    list = []
    for i in range(10): 
        x = float(input())
        list.append(x)
    print("Your list: ",list)
    list = sorted(list)

    notneg = [num for num in list if num >= 0] 
    avg = sum(notneg) / len(notneg) if notneg else 0 

    print(f"MAX = {list.pop()}\nMIN = {list[0]}\nAVG = {avg}")
    pass
ins()