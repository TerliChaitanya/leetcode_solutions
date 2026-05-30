class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        answ=0
        li=[]
        for i in range(0,len(s)):
            li.insert(i,s[i])
            if len(li)>3:
                del li[0]
            if len(set(li))==3:
                answ+=1
        return answ
            
