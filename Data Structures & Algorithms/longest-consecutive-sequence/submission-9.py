class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        series = {}

        for num in set(nums):
            if num - 1 in series and num + 1 in series:
                new_number = (series[num - 1] + series[num + 1]) + 1
                for n in range(num - series[num - 1], num + series[num + 1] + 1):
                    series[n] = new_number
            elif num - 1 in series:
                new_number = series[num - 1] + 1
                for n in range(num - series[num - 1], num + 1):
                    series[n] = new_number
            elif num + 1 in series:
                new_number = series[num + 1] + 1
                for n in range(num, series[num + 1] + 1):
                    series[n] = new_number
            else:
                series[num] = 1

            print(series)

        return max(list(series.values()))

        