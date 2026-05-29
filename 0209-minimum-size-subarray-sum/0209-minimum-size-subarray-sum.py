class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size=float('inf')
        l,r=0,0
        win_sum=0
        while(r<len(nums)):
            win_sum+=nums[r]
            while(win_sum>=target):
                size=min(size,r-l+1)
                win_sum-=nums[l]
                l+=1
            r+=1
        if size==float('inf'):
            return 0
        return size
