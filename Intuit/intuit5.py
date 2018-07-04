t = int(input())
for _ in range(t):
    a = int(input())
    print(*sorted(list(map(int,input().split()))))