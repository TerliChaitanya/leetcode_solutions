class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answ=0
        prefix=0
        dici={0:1}
        for r in range(len(nums)):
            prefix+=nums[r]
            answ+=dici.get(prefix-k,0)
            dici[prefix]=dici.get(prefix,0)+1
        return answ