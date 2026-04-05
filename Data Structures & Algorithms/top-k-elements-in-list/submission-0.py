class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        mc = c.most_common(k)

        answer = []
        for n, _ in mc:
            answer.append(n)

        return answer