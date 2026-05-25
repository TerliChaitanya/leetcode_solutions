class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dicti={}
        if len(set(s))!=len(set(t)):
            return False
        for i in range(0,len(s)):
            if s[i] in dicti:
                if dicti[s[i]]!=t[i]:
                    return False
            else:
                dicti[s[i]]=t[i]
        return True
            