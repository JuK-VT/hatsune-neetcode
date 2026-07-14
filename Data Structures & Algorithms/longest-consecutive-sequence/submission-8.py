class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        series = {}

        for num in set(nums):
            if num - 1 in series and num + 1 in series:
                print("ambos")
                print(num)
                new_number = (series[num - 1] + series[num + 1]) + 1
                for n in range(num - series[num - 1], num + series[num + 1] + 1):
                    print(n)
                    series[n] = new_number
            elif num - 1 in series:
                print("menos 1")
                new_number = series[num - 1] + 1
                for n in range(num - series[num - 1], num + 1):
                    series[n] = new_number
            elif num + 1 in series:
                print("mas 1")
                new_number = series[num + 1] + 1
                for n in range(num, series[num + 1] + 1):
                    series[n] = new_number
            else:
                print("ninguno")
                series[num] = 1

            print(series)

        return max(list(series.values()))

        