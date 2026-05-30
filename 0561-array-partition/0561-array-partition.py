class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        answ=0
        for i in range(0,len(nums),2):
            answ+=nums[i]
        return answ