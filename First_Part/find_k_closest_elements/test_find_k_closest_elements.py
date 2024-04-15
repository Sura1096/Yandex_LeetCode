from find_k_closest_elements import Solution
import pytest

sol = Solution()


class TestFindClosestElements:
    @pytest.mark.parametrize('array, k, x, expected_result', [([1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]),
                                                              ([1, 2, 3, 4, 5], 4, -1, [1, 2, 3, 4]),
                                                              ([1], 1, 10, [1])])
    def test_findClosestElements_func(self, array, k, x, expected_result):
        assert sol.findClosestElements(array, k, x) == expected_result


class TestErrors:
    @pytest.mark.parametrize('array, k, x', [([1, 2, 3, 4, 5], 4, "a"),
                                             ([1, 2, 3, 4, 5], 4, "-1")])
    def test_type_error(self, array, k, x):
        with pytest.raises(TypeError):
            sol.findClosestElements(array, k, x)

    @pytest.mark.parametrize('array, k, x', [([1, 2, 3, 4, 5], "4", 3),
                                             ([1, 2, 3, 4, 5], "4", -1)])
    def test_index_error(self, array, k, x):
        with pytest.raises(IndexError):
            sol.findClosestElements(array, k, x)


class TestConstraints:
    @pytest.mark.parametrize('array, k, x', [([1, 2, 3, 4, 5], 4, 3),
                                             ([1, 2, 3, 4, 5], 4, -1),
                                             ([1], 1, 10)])
    def test_k_constraints(self, array, k, x):
        assert 1 <= k <= len(array)

    @pytest.mark.parametrize('array, k, x', [([1, 2, 3, 4, 5], 4, 3),
                                             ([1, 2, 3, 4, 5], 4, -1),
                                             ([1], 1, 10)])
    def test_k_constraints(self, array, k, x):
        assert -10**4 <= x <= 10**4

    @pytest.mark.parametrize('array, k, x', [([1, 2, 3, 4, 5], 4, 3),
                                             ([1, 2, 3, 4, 5], 4, -1),
                                             ([1], 1, 10)])
    def test_array_length(self, array, k, x):
        assert 1 <= len(array) <= 10**4

    @pytest.mark.parametrize('array, k, x', [([1, 2, 3, 4, 5], 4, 3),
                                             ([1, 2, 3, 4, 5], 4, -1),
                                             ([1], 1, 10)])
    def test_array_consistency(self, array, k, x):
        assert array == array.sort()