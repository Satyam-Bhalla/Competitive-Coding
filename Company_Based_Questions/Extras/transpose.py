n,m= map(int,input().split())
list1 = []
for i in range(n):
    list1.append(list(map(int,input().split())))
list2 = list(zip(*list1))
for i in list2:
    print(*i)