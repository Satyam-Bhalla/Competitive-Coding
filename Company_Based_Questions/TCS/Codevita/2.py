def swap(a,b):
    temp = l[a]
    l[a] = l[b]
    l[b] = temp
    return l[a]*l[b]
n,m = map(int,input().split())
l = list(map(int,input().split()))
m = m-1
result = 0
mine = min(l)
maxe = max(l)
if max(l)==l[m]:
    del l[m]
elif max(l)==l[-1]:
    del l[-1]
else:
    result = swap(l.index(mine),m)
    result += swap(m,l.index(maxe))
    del l[m]
while len(l)>0:
    if l[-1]==max(l):
        del l[-1]
        continue
    else:
        if mine==l[-1]:
            result += swap(l.index(mine),l.index(max(l)))
            del l[l.index(max(l))]
        else:
            result += swap(l.index(mine),l.index(l[-1]))
print(result,end='')