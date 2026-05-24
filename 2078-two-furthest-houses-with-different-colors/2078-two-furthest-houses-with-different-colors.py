class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans=1
        for i in range (0,len(colors)):
            if colors[len(colors)-1]!=colors[i]:
                ans=max(ans,abs(len(colors)-1-i))
        for i in range(len(colors)-1,-1,-1):
            if colors[i]!=colors[0]:
                ans=max(ans,abs(0-i))
        return ans