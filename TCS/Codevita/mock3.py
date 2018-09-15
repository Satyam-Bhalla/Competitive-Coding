n,k = map(int,input().split())
l = list(map(int,input().split()))
for i in range(k):
    count = 0
    lower,upper = map(int,input().split())
    for j in l:
        if j>=lower and j<=upper:
            count += 1
    print(count)