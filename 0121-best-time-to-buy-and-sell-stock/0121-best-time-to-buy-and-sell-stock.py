class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        maxi=0
        for i in range(1,len(prices)):
            if mini>prices[i]:
                mini=prices[i]
            if prices[i]-mini > maxi:
                maxi=prices[i]-mini
        return maxi
        