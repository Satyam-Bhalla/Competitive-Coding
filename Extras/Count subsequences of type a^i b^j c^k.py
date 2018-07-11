#code
t = int(input())
for _ in range(t):
    s = input()
    acount = 0
    bcount = 0
    ccount = 0
    for i in s:
        if i=='a':
            acount = 1+2*acount
        elif i =='b':
            bcount = acount+2*bcount
        elif i=='c':
            ccount = bcount+2*ccount
    print(ccount)