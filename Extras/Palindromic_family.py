t = int(input())
for _ in range(t):
    s = input()
    a = s[::-1]
    odd = s[0::2]
    odd1 = odd[::-1]
    even = s[1::2]
    even1 = even[::-1]
    if a==s:
        print('PARENT')
        continue
    elif odd==odd1 and even==even1:
        print('TWIN')
    elif odd==odd1:
        print('ODD')
    elif even==even1:
        print('EVEN')
    else:
        print('ALIEN')