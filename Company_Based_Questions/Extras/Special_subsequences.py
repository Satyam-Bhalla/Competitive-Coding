from itertools import combinations
from copy import deepcopy
t = int(input())
for _ in range(t):
    s = list(input())
    n = len(s)
    l = []
    m = []
    for k in range(n+1):
        s1 = deepcopy(s)
        for i in range(k):
            s1[i] = s1[i].upper()
        for i in range(1,n+1):
            l.append(list(combinations(s1,i)))
    for i in range(1,n):
        s2 = deepcopy(s)
        s2[i] = s2[i].upper()
        for i in range(1,n+1):
            l.append(list(combinations(s2,i)))
    # for i in range(1,n):
    #     s3 = deepcopy(s)
    #     s3[i] = s3[i].upper()
    #     for i in range(1,n+1):
    #         l.append(list(combinations(s2,i)))
    count = 0
    for i in l:
        for j in i:
            count += 1 
            m.append("".join(j))
    print(len(set(m)),*list(sorted(set(m))),sep="\n")