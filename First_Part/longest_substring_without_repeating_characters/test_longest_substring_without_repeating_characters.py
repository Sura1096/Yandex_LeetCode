import unittest
from longest_substring_without_repeating_characters import Solution


class TestLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_function_output(self):
        self.assertEqual(
            self.sol.lengthOfLongestSubstring("abcabcbb"),
            3
        )

        self.assertEqual(
            self.sol.lengthOfLongestSubstring("bbbbbbb"),
            1
        )

        self.assertEqual(
            self.sol.lengthOfLongestSubstring("pwwkew"),
            3
        )

        self.assertEqual(
            self.sol.lengthOfLongestSubstring("dvdf"),
            3
        )

        self.assertEqual(
            self.sol.lengthOfLongestSubstring(""),
            0
        )

        self.assertEqual(
            self.sol.lengthOfLongestSubstring(" "),
            1
        )

        self.assertEqual(
            self.sol.lengthOfLongestSubstring("tmmzuxt"),
            5
        )


if __name__ == '__main__':
    unittest.main()