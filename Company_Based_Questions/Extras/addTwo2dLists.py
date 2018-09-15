n,m= map(int,input().split())
list1 = []
list2 = []
for i in range(n):
    list1.append(list(map(int,input().split())))
p,q = map(int,input().split())
for i in range(p):
    list2.append(list(map(int,input().split())))
list3 = [[sum(x) for x in zip(list1[i],list2[i])] for i in range(n)]
for i in list3:
    print(*i)