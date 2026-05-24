class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxi=-1
        lower=nums[0]
        for i in range(1,len(nums)):
            if nums[i]-lower!=0:
                maxi=max(maxi,nums[i]-lower)
            lower=min(lower,nums[i])
        return maxi