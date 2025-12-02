from solutions.leetcode_solutions import Solution, VisualizedSolution

def test_two_sum():
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([1, 2, 3, 4], 7) == [2, 3]
    assert s.twoSum([3, 3], 6) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]

def test_length_of_longest_substring():
    s = Solution()
    assert s.lengthOfLongestSubstring("abcabcbb") == 3
    assert s.lengthOfLongestSubstring("bbbbb") == 1
    assert s.lengthOfLongestSubstring("pwwkew") == 3
    assert s.lengthOfLongestSubstring("abcdefghijklmnopqrstuvwxyz") == 26

def test_max_area_trace_visualizer():
    vs = VisualizedSolution()
    best, trace = vs.maxArea_trace([1, 8, 6, 2, 5, 4, 8, 3, 7])
    assert best == 49
    assert trace[0][0] == "frame"
    assert trace[0][1] == 0 and trace[0][2] == 8
    assert any(frame[3] == 49 for frame in trace)
