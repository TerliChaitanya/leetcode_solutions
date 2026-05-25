class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dicti={}
        answ=""
        value=97
        dicti[' ']=' '
        for i in key:
            if i not in dicti:
                dicti[i]=chr(value)
                value+=1
        for i in message:
            answ+=dicti[i]
        return answ
        