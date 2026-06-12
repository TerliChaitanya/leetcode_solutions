class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        li=len(nums)
        while l<=r:
            mid=l+((r-l)//2)
            if (nums[mid]<target):
                l=mid+1
            else:
                li=mid
                r=mid-1
        return li

            
