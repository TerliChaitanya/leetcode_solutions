class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ=sum(nums[:k])
        maxi=summ
        for i in range(k,len(nums)):
            summ-=nums[i-k]
            summ+=nums[i]
            maxi=max(maxi,summ)
        return maxi/k