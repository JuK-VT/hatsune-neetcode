class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = -1
        for i in range(len(nums)):
            if nums[i] == 0 and zeros > -1:
                return [0] * len(nums)
            if nums[i] == 0 and zeros == -1:
                zeros = i
                continue
            product *= nums[i]
        
        if zeros != -1:
            return ([0] * (zeros)) + [product] + ([0] * (len(nums) - zeros - 1))

        return [int(product/num) for num in nums]

        