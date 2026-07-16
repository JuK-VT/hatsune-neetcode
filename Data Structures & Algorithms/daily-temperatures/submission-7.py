class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(0, temperatures[0])]
        res = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                idx, t = stack.pop()
                res[idx] = i - idx
            stack.append((i, temperatures[i]))

        return res
        