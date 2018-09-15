t = int(input())
for _ in range(t):
    a,d,k = map(int,input().split())
    sum = a
    l = []
    if k<d:
      print(-1)
    elif a%2!=0 and d%2==0 and k%2==0:
      print(-1)
    else:
      while True:
          sum += d
          if sum%k==0:
              print(sum//k)
              break
          else:
              if sum%k in l:
                  print(-1)
                  break
              else:
                  l.append(sum%k)