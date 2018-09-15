# A Dynamic Programming based Python Program for the Egg Dropping Puzzle
INT_MAX = 10000000000
def eggDrop(n, k):
    eggFloor = [[0 for x in range(k+1)] for x in range(n+1)]
    for i in range(1, n+1):
        eggFloor[i][1] = 1
        eggFloor[i][0] = 0
    for j in range(1, k+1):
        eggFloor[1][j] = j
 
    # Fill rest of the entries in table using optimal substructure property
    for i in range(2, n+1):
        for j in range(2, k+1):
            eggFloor[i][j] = INT_MAX
            for x in range(1, j+1):
                res = 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x])
                if res < eggFloor[i][j]:
                    eggFloor[i][j] = res
 
    # eggFloor[n][k] holds the result
    return eggFloor[n][k]
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    print(eggDrop(n,k))