#code
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    if n==1:
        n=2
    print(*[p for p in range(n,m+1) if 0 not in [p%d for d in range(2,p)]])