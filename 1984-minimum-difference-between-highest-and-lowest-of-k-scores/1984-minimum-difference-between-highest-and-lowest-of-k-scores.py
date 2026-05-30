class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        answ=float("inf")
        if len(nums)==1:
            return 0
        nums.sort()
        for i in range(0,len(nums)-k+1):
            answ=min(answ,nums[k-1+i]-nums[i])
        return answ