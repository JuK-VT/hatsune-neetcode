class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = 1
        zeroes = 0
        index = -1

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes += 1
                index = i
                if zeroes > 1:
                    return [0] * len(nums)
                continue

            result *= nums[i]

        if zeroes == 1:
            result_list = [0] * len(nums)
            result_list[index] = result
            return result_list

        result_list = []
        for num in nums:
            result_list.append(int(result/num))

        return result_list
