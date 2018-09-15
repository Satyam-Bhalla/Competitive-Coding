from string import ascii_lowercase,ascii_uppercase
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    l = len(s)
    lower = []
    upper = []
    for i in range(l):
        if s[i] in ascii_lowercase:
            lower.append(s[i])
        else:
            upper.append(s[i])
    lower.sort()
    upper.sort()
    k = 0
    j = 0
    for i in range(l):
        if s[i] in ascii_lowercase:
            print(lower[k],sep='',end='')
            k += 1
        else:
            print(upper[j],sep='',end='')
            j += 1
    print()