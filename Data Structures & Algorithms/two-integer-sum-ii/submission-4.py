class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            print(numbers[i], numbers[j])
            if numbers[i] + numbers[j] > target:
                print("entre primero")
                print(numbers[j], numbers[i] + numbers[j], target)
                j -= 1
                continue
            
            if numbers[i] + numbers[j] < target:
                print("entre segundo")
                i += 1
                continue
            
            return [i + 1, j + 1]
