t = int(input())
for _ in range(t):
    n = int(input())
    l1 = set(list(map(int,input().split())))
    l2 = set(list(map(int,input().split())))
    if l1==l2:
        print(1)
    else:
        print(0)