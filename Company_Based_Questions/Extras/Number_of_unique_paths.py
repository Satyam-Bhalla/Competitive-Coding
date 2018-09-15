# Given a M X N matrix with initial position at top-left corner, find the number of possible unique
#  paths to reach the bottom right corner of the grid from the initial position.
t = int(input())
def numberOfPaths(m, n):
   if(m == 1 or n == 1):
        return 1
   return  numberOfPaths(m-1, n) + numberOfPaths(m, n-1)
for _ in range(t):
    m,n = map(int,input().split())
    print(numberOfPaths(m,n))