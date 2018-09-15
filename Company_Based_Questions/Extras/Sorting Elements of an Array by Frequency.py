from collections import Counter
#code
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    c = Counter(l)
    l1 = sorted(sorted(l),key=c.get,reverse=True)
    print(*l1)