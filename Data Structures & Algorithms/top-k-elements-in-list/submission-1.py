class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        result = []
        sorted_keys = sorted(freq, key=freq.get, reverse=True)

        for i in range(k):
            result.append(sorted_keys[i])

        return result