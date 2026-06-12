class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def equaldici(sdici,pdici):
            if len(sdici)!=len(pdici):
                return False
            for i in sdici:
                if i not in pdici or sdici[i]!=pdici[i]:
                    return False
            return True

        pdici={}
        for i in p:
            if i not in pdici:
                pdici[i]=1
            else:
                pdici[i]+=1
        li=[]
        sdici={}
        l=0
        for r in range(len(s)):
            if s[r] not in sdici:
                sdici[s[r]]=1
            else:
                sdici[s[r]]+=1
            if r-l==len(p):
                sdici[s[l]]-=1
                if sdici[s[l]]==0:
                    del sdici[s[l]]
                l+=1
            if equaldici(sdici,pdici):
                li.append(l)
        return li


