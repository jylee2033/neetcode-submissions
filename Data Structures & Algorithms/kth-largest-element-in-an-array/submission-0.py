class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # [2,3,1,1,5,5,4]
        # [1,1,2,3,4,5,5] k = 3
        # 4

        nums.sort()
        return nums[-k]