class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(lambda: 0)

        for num in nums:
            frequency[num] += 1

        frequency_tupl = [(key, value) for key, value in frequency.items()]
        frequency_tupl = sorted(frequency_tupl, key=lambda x: x[1], reverse=True)

        print(frequency_tupl)
        print(frequency_tupl[k:])

        return [number for number, frequ in frequency_tupl[:k]]
        