from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        mag_count = Counter(magazine)
        for c in ransomNote:
            if mag_count[c] == 0:
                return False
            mag_count[c] -= 1
        return True
        
