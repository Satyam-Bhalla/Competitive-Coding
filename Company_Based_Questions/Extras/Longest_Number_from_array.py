from functools import cmp_to_key
def compare(a,b):
    if a+b>b+a:
        return -1
    elif a+b<b+a:
        return 1
    else:
        return 0
t = int(input())
for _ in range(t):
    n = int(input())
    l = sorted(list(input().split()),key=cmp_to_key(compare),reverse=True)
    print("".join(l[::-1]))