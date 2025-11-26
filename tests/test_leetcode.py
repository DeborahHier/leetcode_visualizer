from solutions.leetcode_solutions import Solution

def test_two_sum():
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([1, 2, 3, 4], 7) == [2, 3]
    assert s.twoSum([3, 3], 6) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]

