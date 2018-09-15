from functools import reduce
n = int(input())
for _ in range(n):
    a = int(input())
    l = list(map(int,input().split()))
    print(*[reduce(lambda x,y:x*y,l)//i for i in l])