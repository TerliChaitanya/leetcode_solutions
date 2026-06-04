class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l=0
        temp=0
        ans=0
        cnt1=0
        cnt0=0
        for r in range(len(answerKey)):
            if answerKey[r]=='F':
                cnt0+=1
            else:
                cnt1+=1
            while min(cnt1,cnt0)>k:
                if answerKey[l]=='F':
                    cnt0-=1
                else:
                    cnt1-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans