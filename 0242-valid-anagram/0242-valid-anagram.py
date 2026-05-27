class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t) or set(s)!=set(t):
            return False
        dici1={}
        dici2={}
        for i in range(0,len(s)):
            if s[i] not in dici1:
                dici1[s[i]]=1
            else:
                dici1[s[i]]+=1
            if t[i] not in dici2:
                dici2[t[i]]=1
            else:
                dici2[t[i]]+=1
        for key in s:
            if dici1[key]!=dici2[key]:
                return False
        return True
        