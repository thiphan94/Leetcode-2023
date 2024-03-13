class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 0 if not s else 1 + (s != s[::-1])
