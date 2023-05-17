# ----------DO NOT MODIFY CODE ABOVE THIS ROW, IT WILL ANYWAY BE RESET BEFORE EXECUTION----------
def pick_two(intlist):
    result = []
    total_num = len(intlist)
    for index in range(0,total_num - 1):#(0,3)
        num = intlist[index]#1
        next_index = index+1#1
        while next_index < total_num:#1<=4
        #for next_index in range(index+1, total_num):#(1,4)
            next_num = intlist[next_index]#2
            if num + next_num == 1000:
                result.append(num)
                result.append(next_num)
            break
    return result


N = [1,2,999]
m = [1,2,998,999]
o = [1,2,997]
p = [500,3,2]
q = [1,2,998,990]
output = pick_two(m)
print(output)
