t = int(input())
for _ in range(t):
    a = int(input())
    l = list(map(int,input().split()))
    m = [x for x in range(1,a+1)]
    for i in m:
        if i not in l:
            print(i)
            break
