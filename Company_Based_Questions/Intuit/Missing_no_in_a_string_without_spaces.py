# Given a string consisting of some numbers, not separated by any separator.
# The numbers are positive integers and the sequence increases by one at each
# number except the missing number. The task is to complete the function missingNumber
# which return's the missing number. The numbers will have no more than six digits.
# Print -1 if input sequence is not valid.
t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    for i in range(1,7):
        l = []
        missing = []
        flag = False
        for k in range(0,n,i):
            l.append(int(s[k:k+i]))
        for j in range(len(l)-1):
            a = str(l[j]+1)
            if a == int(s[j:j+i])+1:
                flag = True
                print(flag)
            if flag and a != int(s[j:j+i])+1:
                missing.append(l[j]+1)
        if len(missing)>1:
            print(-1)
            break
        else:
            print(l,missing)