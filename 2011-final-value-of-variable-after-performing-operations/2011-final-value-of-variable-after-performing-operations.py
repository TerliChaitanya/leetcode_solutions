class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        an=0
        for i in operations:
            if i=="++X" or i=="X++":
                an+=1
            else:
                an-=1
        return an
