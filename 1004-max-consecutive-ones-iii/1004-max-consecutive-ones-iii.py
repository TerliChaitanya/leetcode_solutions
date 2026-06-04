class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans=0
        temp_k=0
        l=0
        for r in range(len(nums)):
            if nums[r]!=1:
                temp_k+=1
            while temp_k>k:
                if nums[l]==0:
                    temp_k-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans