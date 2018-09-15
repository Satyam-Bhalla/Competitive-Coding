a=set([0, 4, 5, 6, 7, 8, 9])
t=int(input())
for _ in range(t):
    N=int(input())
    A=input().split()
    Ans=[]
    for i in range (0,N):
        temp=A[i]
        temp=list(temp)
        temp = set(list(map(int, temp)))
        if not(a & temp):
            Ans.append(A[i])
    Ans = sorted(list(map(int, Ans)),key=lambda e: int(e))
    length=len(Ans)
    if not length:
        print("-1")
    else:
        print (*Ans,sep=' ')