t = int(input())
for _ in range(t):
    a,b = input().split()
    l = min(len(a),len(b))
    m = max(len(a),len(b))
    for i in range(l):
        print(a[i],b[i],sep='',end='')
    if m==len(a):
        print(a[l:],sep='',end='')
    else:
        print(b[l:],sep='',end='')
    print()