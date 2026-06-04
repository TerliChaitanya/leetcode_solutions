class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        ans=0
        dici={}
        for i in range(len(fruits)):
            if fruits[i] not in dici:
                dici[fruits[i]]=1
            else:
                dici[fruits[i]]+=1
            while len(dici)>2:
                dici[fruits[l]]-=1
                if dici[fruits[l]]==0:
                    del dici[fruits[l]]
                l+=1
            ans=max(ans,i-l+1)
        return ans