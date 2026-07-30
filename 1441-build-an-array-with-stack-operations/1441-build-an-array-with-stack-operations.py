class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s=set(target)
        ans=[]
        for i in range(1,n+1):
            if i>target[-1]:
                return ans
            ans.append("Push")
            if i not in s:
                ans.append("Pop")
        return ans