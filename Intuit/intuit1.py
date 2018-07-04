
def test(n, arr):
    left_max = arr[0]
    for i in range(1, n):
        if arr[i] < left_max:
            continue
        else: 
            left_max = arr[i]
            for j in range(i+1, n):
                if arr[i] > arr[j]:
                    break
                if j == n-1 and arr[i] <= arr[j]:
                    return arr[i]
    return -1

T = int(input())
for i in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    print(test(n, arr))