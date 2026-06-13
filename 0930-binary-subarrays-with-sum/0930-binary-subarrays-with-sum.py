class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atmost(nums,goal):
            if goal<0:
                return 0
            l=0
            answ=0
            temp=0
            for r in range(len(nums)):
                temp+=nums[r]
                while temp>goal:
                    if nums[l]==1:
                        temp-=1
                    l+=1
                answ+=r-l+1
            return answ
        return atmost(nums,goal)-atmost(nums,goal-1)

