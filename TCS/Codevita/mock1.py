n = int(input())
l = list(map(int,input().split(', ')))
for i in range(len(l)):
    num = l[i]
    a = 0
    while num>0:
        a += num%6
        num = num//6
    l[i] = a
count = 0
for i in range(n):
    for j in range(i,n):
        if l[i]>l[j]:
            count += 1
print(count)