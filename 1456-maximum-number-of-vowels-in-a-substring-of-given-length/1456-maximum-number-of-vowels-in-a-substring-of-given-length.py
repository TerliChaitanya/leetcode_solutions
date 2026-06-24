class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        sets={'a','e','i','o','u'}
        l=0
        temp=0
        maxi=0
        for i in range(len(s)):
            if s[i] in sets:
                temp+=1
            if i-l+1>k:
                if s[l] in sets:
                    temp-=1
                l+=1
            maxi=max(maxi,temp)
        return maxi

        