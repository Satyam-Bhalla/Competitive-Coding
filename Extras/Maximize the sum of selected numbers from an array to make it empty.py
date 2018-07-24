#code
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    sum = 0
    while True:
        a = max(l)
        sum += a
        if a-1 in l:
            l.remove(a-1)
        l.remove(a)
        if len(l)==0:
            print(sum)    
            break