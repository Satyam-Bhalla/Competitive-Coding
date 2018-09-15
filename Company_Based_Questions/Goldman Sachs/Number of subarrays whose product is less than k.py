def countsubarray(nums, k):
    if k <= 1: return 0
    prod = 1
    ans = left = 0
    for right, val in enumerate(nums):
        prod *= val
        while prod >= k:
            prod /= nums[left]
            left += 1
        ans += right - left + 1
    return ans
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    print(countsubarray(l,k))