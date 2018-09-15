t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(n):
        print(len([a for a in bin(int(input()))[2:] if a=='1']))