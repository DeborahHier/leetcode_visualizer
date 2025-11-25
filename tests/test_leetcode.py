from solutions.leetcode_solutions import Solution

def test_two_sum():
    problems = Solution()
    assert problems.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert problems.twoSum([1, 2, 3, 4], 7) == [2, 3]