class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        answ=0
        for i in range(len(s)-2):
            for j in range(i+1,len(s)-1):
                for k in range(j+1,len(s)):
                    if k-j==1 and j-i==1:
                        if s[i]!=s[j] and s[j]!=s[k] and s[i]!=s[k]:
                            answ+=1
        return answ
