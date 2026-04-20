class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            total = nums[l] + nums[r] + nums[i]

            while l < r:
                total = nums[l] + nums[r] + nums[i]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                elif total == 0:
                    if sorted([nums[l], nums[r], nums[i]]) not in output:
                        output.append(sorted([nums[l], nums[r], nums[i]]))
                    l += 1

        return output