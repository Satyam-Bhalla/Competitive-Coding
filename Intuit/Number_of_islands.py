def getRegionSize(matrix,row,column):
    if row < 0 or column < 0 or row >= len(matrix) or column >= len(matrix[row]):
        return 0
    if matrix[row][column] == 0:
        return 0
    matrix[row][column] = 0
    size = 1
    for r in range(row-1,row+2):
        for c in range(column-1,column+2):
            if r != row or c != column:
                size += getRegionSize(matrix,r,c)
    return size


def findIslands(matrix, n, m):
    size = 0
    l = []
    for row in range(n):
        for column in range(m):
            if matrix[row][column] == 1:
                size = getRegionSize(matrix,row,column)
                l.append(size)
    return len(l)



if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[1])]for j in range(n[0])]
        c=0
        for i in range(n[0]):
            for j in range(n[1]):
                matrix[i][j] = arr[c]
                c+=1
        print(findIslands(matrix, n[0], n[1]))