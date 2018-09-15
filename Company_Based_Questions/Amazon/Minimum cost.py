# code
t = int(input())
for _ in range(t):
    n = int(input())
    temp = list(map(int, input().split()))
    l = [temp[i:i+n] for i in range(0, len(temp), n)]
    del temp
    weight = 1
    for i in range(n):
        l.append(list(map(int, input().split(','))))
    row = 0
    col = 0
    suml = 0
    while True:
        if row < n-1 and col < n-1:
            a = min(l[row+1][col], l[row][col+1])
            if a == l[row+1][col]:
                row += 1
            else:
                col += 1
            suml += a
        if row == n-1 and col < n-1:
            col += 1
            a = l[row][col]
            suml += a
        if row < n-1 and col == n-1:
            row += 1
            a = l[row][col]
            suml += a
        if row == n-1 and col == n-1:
            a = l[row][col]
            suml += a
            print(suml)
            break
