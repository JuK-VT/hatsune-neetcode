class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        series = {}
        consecutives = 0

        for num in set(nums):
            if num - 1 in series and num + 1 in series:
                new_number = (series[num - 1] + series[num + 1]) + 1
                series[num - series[num - 1]] = new_number
                series[num + series[num + 1]] = new_number
                if consecutives < new_number:
                    consecutives = new_number
            elif num - 1 in series:
                new_number = series[num - 1] + 1
                series[num - series[num - 1]] = new_number
                series[num] = new_number
                if consecutives < new_number:
                    consecutives = new_number
            elif num + 1 in series:
                new_number = series[num + 1] + 1
                series[num + series[num + 1]] = new_number
                series[num] = new_number
                if consecutives < new_number:
                    consecutives = new_number
            else:
                series[num] = 1
                if consecutives < 1:
                    consecutives = 1

        return consecutives
