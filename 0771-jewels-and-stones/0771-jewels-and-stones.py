class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set=set(jewels)
        an=0
        for i in stones:
            if i in jewels:
                an+=1
        return an