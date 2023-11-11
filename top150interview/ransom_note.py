from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # for elt in set(ransomNote):
        #     if ransomNote.count(elt)>magazine.count(elt):return False
        # return True
        ransom_counts = Counter(ransomNote)
        magazine_counts = Counter(magazine)

        return all(
            ransom_counts[char] <= magazine_counts[char] for char in set(ransomNote)
        )
