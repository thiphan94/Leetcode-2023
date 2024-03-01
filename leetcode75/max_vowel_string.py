class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]

        n = len(s)

        if n < k:
            return -1

        window_sum = sum(1 for char in s[:k] if char in vowels)

        max_sum = window_sum

        for i in range(n - k):
            pre = 1 if s[i] in vowels else 0
            following = 1 if s[i + k] in vowels else 0
            window_sum = window_sum - pre + following
            max_sum = max(window_sum, max_sum)

        return max_sum
