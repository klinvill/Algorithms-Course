__author__ = 'Kirby'

from inversions import countCrossInversions, countInversions

class TestCountCrossInversions:
    def test_no_cross_inversions(self):
        left = [1, 2, 3]
        right = [4, 5, 6]
        merged, count = countCrossInversions(left, right)
        assert count == 0
        assert merged == [1, 2, 3, 4, 5, 6]

    def test_singlespot_single_cross_inversion(self):
        left = [1, 2, 4]
        right = [3, 5, 6]
        merged, count = countCrossInversions(left, right)
        assert count == 1
        assert merged == [1, 2, 3, 4, 5, 6]

    def test_multispot_single_cross_inversion(self):
        left = [1, 3, 4]
        right = [2, 5, 6]
        merged, count = countCrossInversions(left, right)
        assert count == 2
        assert merged == [1, 2, 3, 4, 5, 6]

    def test_multiple_cross_inversions(self):
        left = [3, 4, 5]
        right = [1, 2, 6]
        merged, count = countCrossInversions(left, right)
        assert count == 6
        assert merged == [1, 2, 3, 4, 5, 6]

    def test_empty_right_cross_inversion(self):
        left = [1, 2, 3]
        right = []
        merged, count = countCrossInversions(left, right)
        assert count == 0
        assert merged == [1, 2, 3]

    def test_empty_left_cross_inversion(self):
        left = []
        right = [1, 2, 3]
        merged, count = countCrossInversions(left, right)
        assert count == 0
        assert merged == [1, 2, 3]

    def test_negative_list_cross_inversion(self):
        left = [-5, -3, 1]
        right = [-2, 2, 3]
        merged, count = countCrossInversions(left, right)
        assert count == 1
        assert merged == [-5, -3, -2, 1, 2, 3]




class TestCountInversions:
    def test_no_inversions(self):
        nums = [1, 2, 3, 4, 5, 6]
        assert countInversions(nums) == 0

    def test_singlespot_single_inversion(self):
        nums = [1, 2, 4, 3, 5, 6]
        assert countInversions(nums) == 1

    def test_multispot_single_inversion(self):
        nums = [1, 4, 2, 3, 5, 6]
        assert countInversions(nums) == 2

    def test_multiple_inversions(self):
        nums = [1, 4, 2, 5, 3, 6]
        assert countInversions(nums) == 3

    def test_single_list_no_inversions(self):
        nums = [1]
        assert countInversions(nums) == 0

    def test_empty_list_no_inversions(self):
        nums = []
        assert countInversions(nums) == 0

    def test_negative_list_inversions(self):
        nums = [-5, 1, -3, 2, -2, 3]
        assert countInversions(nums) == 3

    def test_float_list_inversions(self):
        nums = [1.6, 2.3, 6.3, 3.8, 4.9]
        assert countInversions(nums) == 2


