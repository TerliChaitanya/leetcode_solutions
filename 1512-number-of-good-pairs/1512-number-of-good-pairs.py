class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dicti={}
        count=0
        for i in nums:
            if i not in dicti:
                dicti[i]=1
            else:
                dicti[i]+=1
                count+=dicti[i]-1
        return count