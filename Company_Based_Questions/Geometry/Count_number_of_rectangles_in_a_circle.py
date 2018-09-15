def countRectangles(r):
    d = 2*r
    dSq = d*d
    rectangles = 0
    for i in range(1,d):
        for j in range(1,d):
            if i**2+j**2 <= dSq:
                rectangles += 1
    return rectangles
t = int(input())
for _ in range(t):
    r = int(input())
    print(countRectangles(r))