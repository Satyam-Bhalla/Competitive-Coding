t = int(input())
# Python program to compute sum of pairwise bit differences
 
def sumBitDifferences(arr,n):
    ans = 0  # Initialize result
 
    # traverse over all bits
    for i in range(0, 32):
     
        # count number of elements with i'th bit set
        count = 0
        for j in range(0,n):
            if ( (arr[j] & (1 << i)) ):
                count+=1
 
        # Add "count * (n - count) * 2" to the answer
        ans += (count * (n - count) * 2);
     
    return ans
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    print(sumBitDifferences(l,n))