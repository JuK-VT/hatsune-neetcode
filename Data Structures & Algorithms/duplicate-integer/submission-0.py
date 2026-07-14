class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeated = set(nums)
        return len(nums) > len(repeated)
         