class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len, left = 0, 0
        existed = {}
        for i in range(len(s)):
            if s[i] in existed and existed[s[i]] >= left:
                left = existed[s[i]] + 1
            else:
                max_len = max(max_len, i - left + 1)
            existed[s[i]] = i
        return max_len
