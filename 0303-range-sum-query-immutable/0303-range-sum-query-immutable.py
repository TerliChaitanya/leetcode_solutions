class NumArray:

    def __init__(self, nums: List[int]):
        self.prenum=[0]
        for i in range(len(nums)):
            self.prenum.append(self.prenum[i]+nums[i])
    def sumRange(self, left: int, right: int) -> int:
        return self.prenum[right+1]-self.prenum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)