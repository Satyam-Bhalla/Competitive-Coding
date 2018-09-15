s,n,k,m = map(int,input().split())
l = list(map(int,input().split()))
dry = n-k
result = 0
l1 = []
for i in l:
    result += i
    l1.append(result)

mine = 1
maxe = l1[-1]
count = maxe-mine
for i in range(len(l)):
    mine = l1[i-1]+1
    while dry+k>0:
        if i%2==0 and dry>0:
            dry = dry-l[i]
        elif k>0:
            k = k-l[i]
    if k<0:
        maxe = l1[i-1]+l[i]+k
        print(maxe)
    if dry<0:
        maxe = l1[i-1]+l[i]+dry
        print(maxe)
    if maxe-mine<count:
        count = maxe-mine
print(count)