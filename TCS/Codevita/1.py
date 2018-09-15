from math import sqrt
def isSquareFree(n):
    if n % 2 == 0:
        n = n / 2
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n) + 1)):
        if n % i == 0:
            n = n / i
        if n % i == 0:
            return False
    return True

def is_square(i):
    return i**0.5 == int(i**0.5)

n = int(input())
l = [i for i in range(2,((n+1)//2)+1) if n%i==0]
if n%2!=2:
    l.append(n)
count = 0
for i in range(len(l)):
    if l[i]!=None and is_square(l[i]):
        for j in range(i+1,len(l)):
            if l[j]%l[i]==0:
                l[j] = None
        l[i]=None
for i in l:
    if i:
        count += 1
print(count)