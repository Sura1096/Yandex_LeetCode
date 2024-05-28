import pytest
from summary_ranges import Solution


sol = Solution()


@pytest.mark.parametrize('nums, expected_result',
                         [([0, 1, 2, 4, 5, 7], ['0->2', '4->5', '7']),
                          ([0, 2, 3, 4, 6, 8, 9], ['0', '2->4', '6', '8->9']),
                          ([1, 2, 3, 4, 5], ['1->5'])])
def test_positive_numbers(nums, expected_result):
    assert sol.summaryRanges(nums) == expected_result


@pytest.mark.parametrize('nums, expected_result',
                         [([-5, -4], ['-5->-4']),
                          ([-7, -3], ['-7', '-3']),
                          ([-4, -3, -2, -1], ['-4->-1']),
                          ([-6, -4, -3, -1], ['-6', '-4->-3', '-1'])])
def test_negative_numbers(nums, expected_result):
    assert sol.summaryRanges(nums) == expected_result
