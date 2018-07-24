def fib(n):
    first = 0
    second = 1
    if n == 1:
       return 1
    elif n == 0:   
       return 0            
    else:
        for i in range(n):
            sum = first + second
            first = second
            second = sum
        return sum
t = int(input())
for _ in range(t):
    first = 0
    second = 1
    sum = 0
    n = int(input())
    print(int(fib(n)))