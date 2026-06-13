class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(nums,k):
            if k<1:
                return 0
            dici={}
            l=0
            answ=0
            temp=0
            for r in range(len(nums)):
                if nums[r] not in dici:
                    temp+=1
                    dici[nums[r]]=1
                else:
                    dici[nums[r]]+=1
                while temp>k:
                    dici[nums[l]]-=1
                    if dici[nums[l]]==0:
                        del dici[nums[l]]
                        temp-=1
                    l+=1
                answ+=r-l+1
            return answ
        return atmost(nums,k)-atmost(nums,k-1)
                