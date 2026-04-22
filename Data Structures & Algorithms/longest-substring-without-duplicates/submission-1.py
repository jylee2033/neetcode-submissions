class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "abba"
        # {"a":0,"b":3}
        # l = b [2]
        # r = a [3]
        # max_count = 2

        # "abcabcbb"
        # {"a":0,"b":1,"c":2}
        # l = a
        # r = a
        # max_count = 0
        
        max_count = 0
        l = 0
        seen = {}

        for r, char in enumerate(s):
            if char in seen and seen[char] >= l:
                l = seen[char] + 1

            seen[char] = r
            max_count = max(max_count, r - l + 1)

        return max_count