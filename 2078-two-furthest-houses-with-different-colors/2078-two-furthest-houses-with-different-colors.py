class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans=1
        for i in range (0,len(colors)):
            for j in range(len(colors)-1,-1,-1):
                if colors[i]!=colors[j]:
                    ans=max(ans,abs(i-j))
        return ans