class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []

        for i in range(len(nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            j, k = i + 1, len(sorted_nums) - 1
            
            while j < k:
                if sorted_nums[j] + sorted_nums[k] < -sorted_nums[i]:
                    j += 1
                elif sorted_nums[j] + sorted_nums[k] > -sorted_nums[i]:
                    k -= 1
                else:
                    res.append([sorted_nums[j], sorted_nums[k], sorted_nums[i]])
                    j += 1
                    while sorted_nums[j] == sorted_nums[j - 1] and j < k:
                        j += 1

        return res
        