class Solution:
    def pivotInteger(self, n: int) -> int:
        left=0
        right=0
        if n==1:
            return 1
        for i in range(1,n+1):
            left+=i
            if left==(n*(n+1)/2-left+i):
                return i
        return -1