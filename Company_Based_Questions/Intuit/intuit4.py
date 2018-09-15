# from itertools import permutations
t = int(input())
for _ in range(t):
    l = input()
    s = list(input())
    # spr = list(permutations(s))
    # sstr = []
    # for i in spr:
    #     sstr.append("".join(i))
    lens = len(s)
    sums = sum(map(lambda x: ord(x),s))
    count = 0
    for i in range(0,len(l)-lens+1):
        if sum(map(lambda x: ord(x),l[i:i+lens]))==sums and all(map(lambda x: x in s,l[i:i+lens])):
            count += 1
    print(count)