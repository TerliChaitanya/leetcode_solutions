class Solution:
    def intToRoman(self, num: int) -> str:
        v=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
        s=['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        v.reverse()
        s.reverse()
        ans=''
        i=0
        while num>0:
            if v[i]>num:
                i+=1
            else:
                ans+=''+s[i]
                num-=v[i]
        return ans
