class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        res=[0]*len(nums)
        i=r
        while(l<=r):
            if nums[l]**2>((nums[r])**2):
                res[i]=nums[l]**2
                i-=1
                l+=1
            else:
                res[i]=nums[r]**2
                i-=1
                r-=1
        return res
            
