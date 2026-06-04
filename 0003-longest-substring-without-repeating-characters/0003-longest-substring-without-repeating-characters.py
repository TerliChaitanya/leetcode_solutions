class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        li=[]
        ans=0
        for r in range(len(s)):
            li.append(s[r])
            while len(set(li))<len(li):
                del li[0]
            ans=max(ans,len(li))
        return ans