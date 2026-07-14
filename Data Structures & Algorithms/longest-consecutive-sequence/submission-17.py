class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)

        startpoints, endpoints = set(), set()

        for num in num_set:
            if num - 1 in num_set and num + 1 not in num_set:
                endpoints.add(num)
            if num - 1 not in num_set and num + 1 in num_set:
                startpoints.add(num)

        startpoints = sorted(startpoints)
        endpoints = sorted(endpoints)

        if not endpoints:
            return 1

        difference = [(endpoints[i] - startpoints[i]) + 1 for i in range(len(endpoints))]

        return max(difference)
