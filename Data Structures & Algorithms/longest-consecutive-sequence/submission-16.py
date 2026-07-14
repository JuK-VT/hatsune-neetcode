class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        series = defaultdict(int)
        consecutives = 0

        for num in nums:
            if not series[num]:
                series[num] = series[num + 1] + series[num - 1] + 1
                series[num - series[num - 1]] = series[num]
                series[num + series[num + 1]] = series[num]
                consecutives = max(consecutives, series[num])

        return consecutives
