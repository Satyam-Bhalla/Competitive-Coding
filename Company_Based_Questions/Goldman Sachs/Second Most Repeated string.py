def sorted_second(val) :
    return val[1]

t= int(input())
for i in range(t):
    n = int(input())
    arr = list(map(str,input().split()))
    str_dict = {}
    for ar in arr :
        if ar not in str_dict :
            str_dict[ar] = 1
        else :
            str_dict[ar] += 1
    print(sorted(str_dict.items(),key=sorted_second,reverse=True)[1][0])
    