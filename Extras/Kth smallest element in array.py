#code
t = int(input())
for _ in range(t):
    n = int(input())
    l = sorted(list(map(int,input().split())))
    k = int(input())
    print(l[k-1])