class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # same color are adjacent
        # 0 red
        # 1 white
        # 2 blue
        # [2,0,1]
        # [0,2,1]

        l = 0
        r = len(nums) - 1
        m = 0

        while m <= r:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1

            elif nums[m] == 2:
                nums[r], nums[m] = nums[m], nums[r]
                r -= 1

            elif nums[m] == 1:
                m += 1