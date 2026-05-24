class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dicti={}
        count=0
        for i in stones:
            if i not in dicti:
                dicti[i]=1
            else:
                dicti[i]+=1
        for i in jewels:
            if i in dicti:
                count+=dicti[i]
        return count
            