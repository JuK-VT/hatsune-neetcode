class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        prefix, postfix = [], []
        for i in range(len(nums)):
            prod *= nums[i]
            prefix.append(prod)

        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            prod *= nums[i]
            postfix.append(prod)

        postfix = list(reversed(postfix))

        print("Prefix: ", prefix)
        print("Postfix: ", postfix)

        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(postfix[i + 1])
            elif i == (len(nums) - 1):
                result.append(prefix[i -1])
            else:
                result.append(prefix[i - 1] * postfix[i + 1])

        return result
