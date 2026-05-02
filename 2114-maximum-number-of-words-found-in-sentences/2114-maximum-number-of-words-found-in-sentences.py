class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        words=[]
        for i in range(len(sentences)):
            words.append(sentences[i].count(' ')+1)
        return max(words)


