from typing import Any
class Solution:
    def twoSum(self, nums, target):
        ht: dict[int, int] = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in ht:
                return [ht[complement], i]
            else:
                ht[num] = i
        
        return []
    
    def lengthOfLongestSubstring(self, s: str) -> int:  
        left = 0
        seen = {}
        max_len = 0

        for right, char in enumerate(s):
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            
            seen[char] = right

            max_len = max(max_len, right - left + 1)
    
        return max_len

class VisualizedSolution:
    def lengthOfLongestSubstring_trace(self, s: str) -> tuple[int, list[Any]]:
        left = 0
        seen = set()
        best = 0
        trace = []

        for right, char in enumerate(s):
            trace.append(("frame", left, right))

            while char in seen:
                seen.remove(s[left])
                left += 1
                trace.append(("frame", left, right))

            seen.add(char)
            best = max(best, right - left + 1)

        return best, trace
