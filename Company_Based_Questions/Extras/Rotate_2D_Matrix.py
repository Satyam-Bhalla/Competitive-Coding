#Rotate 2d matrix by 90 degree
def to_matrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    l = to_matrix(l,n)
    l = list(zip(*l[::-1]))
    for i in l:
        print(*i,end=' ')
    print()