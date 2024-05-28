import pytest
from summary_ranges import Solution


sol = Solution()


@pytest.mark.parametrize('nums, expected_result',
                         [([0, 1, 2, 4, 5, 7], ['0->2', '4->5', '7']),
                          ([0, 2, 3, 4, 6, 8, 9], ['0', '2->4', '6', '8->9']),
                          ([1, 2, 3, 4, 5], ['1->5'])])
def test_positive_numbers(nums, expected_result):
    assert sol.summaryRanges(nums) == expected_result
