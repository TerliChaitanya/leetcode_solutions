class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        answ=0
        cost.sort()
        l=len(cost)-1
        i=1
        while(l>=0):
            if i==3:
                i=1
            else:
                answ+=cost[l]
                i+=1
            l-=1
        return answ