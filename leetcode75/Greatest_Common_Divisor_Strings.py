import unittest

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If str2 is longer than str1
        if len(str1) < len(str2):
            str1, str2 = str2, str1

        # If two strings are identical
        if str1 == str2:
            return str1

        # Recursively call the function
        if str1[:len(str2)] == str2:
            return self.gcdOfStrings(str1[len(str2):], str2)
        
        return ""

class TestGreatestCommonDivisor(unittest.TestCase):
    def test_greatest_common_divisor(self):
        solution = Solution()
        self.assertEqual(solution.gcdOfStrings("ABCABC", "ABC"), "ABC")
        self.assertEqual(solution.gcdOfStrings("ABABAB", "ABAB"), "AB")
        self.assertEqual(solution.gcdOfStrings("LEET", "CODE"), "")

if __name__ == '__main__':
    unittest.main()