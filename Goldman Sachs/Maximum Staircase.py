t = int(input())
for _ in range(t):
    n = int(input())
    a = 1
    while n>=0:
        n -= a
        if n-a>=0:
            a += 1
    print(a) 