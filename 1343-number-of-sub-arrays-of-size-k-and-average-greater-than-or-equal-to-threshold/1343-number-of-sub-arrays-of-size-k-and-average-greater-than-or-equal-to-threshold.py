class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        answ=0
        l=0
        li=[]
        summ=0
        for r in range(len(arr)):
            li.append(arr[r])
            summ+=arr[r]
            if len(li)>k:
                summ-=li[0]
                li.pop(0)
            if len(li)==k and summ/k>=threshold:
                answ+=1
        return answ
