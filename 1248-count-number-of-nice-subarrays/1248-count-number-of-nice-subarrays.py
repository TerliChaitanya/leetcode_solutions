class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def he(nums,k):
            l=0
            answ=0
            tk=0
            for r in range(len(nums)):
                if nums[r]%2==1:
                    tk+=1
                while tk>k:
                    if nums[l]%2==1:
                        tk-=1
                    l+=1
                answ+=r-l+1
            return answ
        return he(nums,k)-he(nums,k-1)      