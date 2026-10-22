from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count=Counter(magazine)
        for ch in ransomNote:
            if magazine_count[ch]==0:
                return False
            else:
                magazine_count[ch]-=1
        return True