# (n^p)%m
t = int(input())
for _ in range(t):
    n,p,m = map(int,input().split())
    if p==0:
        print(1%m)
    ans = 1
    base = n
    while p > 0:
        if p%2 == 1:
            ans = (ans*base)%m
            p -= 1
        else:
            base = (base*base)%m
            p /= 2
    if ans < 0:
        ans = (ans+m)%m
    print(ans)