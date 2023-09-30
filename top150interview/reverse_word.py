class Solution:
    def reverseWords(self, s: str) -> str:
        new_list = s.split()
        new_list.reverse()
        return " ".join(new_list)
