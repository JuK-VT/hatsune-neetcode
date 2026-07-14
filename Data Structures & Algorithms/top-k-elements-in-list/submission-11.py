class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}
        for num in nums:
            if num not in my_map:
                my_map[num] = 0
            my_map[num] += 1

        ranking = sorted(my_map, key=my_map.get, reverse=True)
        return ranking[:k]
        