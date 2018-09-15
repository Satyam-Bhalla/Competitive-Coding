n = int(input())
l = []
weight = 1
for i in range(n):
    l.append(list(map(int,input().split(','))))
row = 0
col = 0
while True:
    if row < n-1 and col < n-1:
        a = min(l[row+1][col],l[row][col+1])
        if a==l[row+1][col]:
            row += 1
        else:
            col += 1
    if row==n-1 and col<n-1:
        col += 1
        a = l[row][col]
    if row<n-1 and col==n-1:
        row += 1
        a = l[row][col]
    if a>weight:
        weight = a 
    if row==n-1 and col==n-1:
        a = l[row][col]
        if a>weight:
            weight = a
        print(weight)
        break
