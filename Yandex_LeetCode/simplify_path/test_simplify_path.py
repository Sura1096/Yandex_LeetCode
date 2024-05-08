import pytest
from simplify_path import Solution


sol = Solution()


@pytest.mark.parametrize('path, expected_result',
                         [("/home/", "/home"),
                          ("/../", "/"),
                          ("/home//foo/", "/home/foo"),
                          ("/home/user/Documents/../Pictures", "/home/user/Pictures"),
                          ("/.../a/../b/c/../d/./", "/.../b/d")])
def test_positive_cases(path, expected_result):
    assert sol.simplifyPath(path) == expected_result
