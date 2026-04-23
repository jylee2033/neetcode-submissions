class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [1,4,3,2], 9
        # k = 2: 1 + 2 + 2 + 1 = 6
        # k = 1: 1 + 4 + 3 + 2 = 10

        # piles=[312884470], 312884469
        # k = 2: 

        l = 1 # 1
        r = max(piles) # 312884470

        while l <= r:
            k = (l + r) // 2 # 2
            total = 0

            for p in piles:
                total += math.ceil(p/k)
            if total <= h:
                r = k - 1
            elif total > h:
                l = k + 1

        return l