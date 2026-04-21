class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "zxyzxyz"
        # l = x
        # r = z
        # count = r - l + 1
        # max_count 3
        # {"z":4, "x":1, "y":2}

        l = 0
        seen = {}
        max_count = 0

        for r, char in enumerate(s):
            if char in seen:
                if seen[char] >= l:
                    l = seen[char] + 1

            seen[char] = r
            max_count = max(max_count, r - l + 1)

        return max_count