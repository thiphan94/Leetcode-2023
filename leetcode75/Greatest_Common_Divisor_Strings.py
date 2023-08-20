import unittest


class Solution:
    """Solution class"""

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """Given two strings, return the largest string x such that x divides both str1 and str2"""
        if len(str1) < len(str2):
            str1, str2 = str2, str1

        if str1 == str2:
            return str1
        if str1[: len(str2)] == str2:
            return self.gcdOfStrings(str1[len(str2) :], str2)

        return ""


class TestGreatestCommonDivisor(unittest.TestCase):
    """Test cases"""

    def test_greatest_common_divisor(self):
        """Test"""
        solution = Solution()
        self.assertEqual(solution.gcdOfStrings("ABCABC", "ABC"), "ABC")
        self.assertEqual(solution.gcdOfStrings("ABABAB", "ABAB"), "AB")
        self.assertEqual(solution.gcdOfStrings("LEET", "CODE"), "")


if __name__ == "__main__":
    unittest.main()
