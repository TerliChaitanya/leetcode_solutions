class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        mp={')':'(','}':'{',']':'['}
        for i in s:
            if i in mp:
                if not a or mp[i]!=a.pop():
                    return False
            else:
                a.append(i)
        return len(a)==0
            