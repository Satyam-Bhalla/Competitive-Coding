#code
t = int(input())
for _ in range(t):
    s = input()
    flag = False
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i]==s[j]:
                print(s[i])
                flag = True
                break
        if flag:
            break
    if not flag:
        print(-1)