from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for elt in strs:
            word = "".join(sorted(elt))
            if word in anagrams:
                anagrams[word].append(elt)
            else:
                anagrams[word] = [elt]
        return anagrams.values()
