class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        se=set()
        answ=0
        for r in range(len(s)):
            if s[r] not in se:
                se.add(s[r])
            else:
                while s[r] in se:
                    se.remove(s[l])
                    l+=1
                se.add(s[r])
            answ=max(answ,r-l+1)
        return answ
        