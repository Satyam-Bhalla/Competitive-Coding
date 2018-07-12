def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    l = []
    for p in range(2, n):
        if prime[p]:
            l.append(p)
    l.pop(0)
    return l
t = int(input())
for _ in range(t):
    n = int(input())
    l =  SieveOfEratosthenes(n)
    length = len(l)
    left = 0
    r = length-1
    while left < r:
        if l[left]+l[r] < n:
            left += 1
        if l[left]+l[r] > n:
            r -= 1
        if l[left]+l[r]==n:
            print(min(l[left],l[r]),max(l[left],l[r]))
            break
