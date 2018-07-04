n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
    l = sorted(l)
    length = len(l)
    if length%2 ==0:
        print((l[length//2]+l[(length//2)-1])//2)
    else:
        print(l[(length//2)])