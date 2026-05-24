class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        di={}
        maxi=floor(len(nums)/2)
        for i in nums:
            if i not in di:
                di[i]=1
            else:
                di[i]+=1
                if di[i]>maxi:
                    return i
        return i
        