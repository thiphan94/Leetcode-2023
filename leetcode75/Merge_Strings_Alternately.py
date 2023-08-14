import unittest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1

        while i < len(word1):
            result.append(word1[i])
            i += 1

        while j < len(word2):
            result.append(word2[j])
            j += 1

        return ''.join(result)

class TestMergeStrings(unittest.TestCase):
    def test_merge_strings(self):
        solution = Solution()
        self.assertEqual(solution.mergeAlternately("abc", "pqr"), "apbqcr")
        self.assertEqual(solution.mergeAlternately("hello", "world"), "hweolrllod")

    def test_merge_strings_different_lengths(self):
        solution = Solution()
        self.assertEqual(solution.mergeAlternately("ab", "pqrs"), "apbqrs")
        self.assertEqual(solution.mergeAlternately("abcd", "pq"), "apbqcd")

if __name__ == '__main__':
    unittest.main()
