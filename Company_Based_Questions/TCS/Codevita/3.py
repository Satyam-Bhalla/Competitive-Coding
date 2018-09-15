from math import sqrt
def factors(n):
    l = []
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            if n//i==i:
                l.append(i)
            else:
                l.append(i)
                l.append(n//i)
    return l
def SquareFree(n):
    if n%2==0:
        n = n//2
    if n%2==0:
        return False
    for i in range(3,int(sqrt(n))+1,2):
        if n%i==0:
            n = n//i
            if n%i==0:
                return False
    return True
if __name__=='__main__':
    n = int(input())
    count = 0
    l = factors(n)
    for i in l:
        if SquareFree(i):
            count += 1
    print(count-1,end='')
