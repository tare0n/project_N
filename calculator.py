def calculator(string):
    list_of_mult = string.split("*")
    for i in range(len(list_of_mult)):
        list_of_mult[i] = list_of_mult[i].split("+")
    for i in range(1,len(list_of_mult)):
        list_of_mult[i][0] = int(list_of_mult[i][0]) * int(list_of_mult[i-1].pop())
    out_list = []
    for i in list_of_mult:
        for j in i:
            out_list.append(int(j))
    return sum(out_list)
