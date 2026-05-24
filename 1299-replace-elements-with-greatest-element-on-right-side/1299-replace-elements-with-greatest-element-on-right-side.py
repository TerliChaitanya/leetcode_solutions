class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        grea=-1
        for i in range(len(arr)-1,-1,-1):
            temp=arr[i]
            arr[i]=grea
            grea=max(grea,temp)
        return arr