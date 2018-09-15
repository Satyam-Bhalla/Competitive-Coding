# Input 1,2,3,4,5,6

l = list(map(int,input().split(',')))
max7=0
max8 = 0
if 2 in l:
    max7 = 2
if 4 in l:
    max8 = 4
if l.count(0)>3 and max7==2 and max8==4:
    print('24:00:00')
    exit()
max1 = 0
k = []
for i in l:
    if i > max1 and i <= 2:
        max1 = i
if max1 in l:
    k.append(max1)
    l.remove(max1)

max2 = 0
for i in l:
    if max1 == 2:
        if i>max2 and i<4:
            max2 = i
    else:
        if i>max2 and i<=9:
            max2 = i
if max2 in l:
    k.append(max2)
    l.remove(max2)

max3 = 0
for i in l:
    if i>max3 and i<=5:
        max3 = i

if max3 in l:
    k.append(max3)
    l.remove(max3)
max4 = 0
for i in l:
    if i>max4 and i<=9:
        max4 = i

if max4 in l:
    k.append(max4)
    l.remove(max4)

max5 = 0
for i in l:
    if i>max5 and i<=5:
        max5 = i

if max5 in l:
    k.append(max5)
    l.remove(max5)
max6 = 0
for i in l:
    if i>max6 and i<=9:
        max6 = i
if max6 in l:
    k.append(max6)
if len(k)<6:
    print('Impossible')
else:
    print(*k[0:2],end=':',sep='')
    print(*k[2:4],end=':',sep='')
    print(*k[4:6],sep='')