class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s_idx = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while s_idx and temperatures[i] > temperatures[s_idx[-1]]:
                res[s_idx[-1]] = i - s_idx[-1]
                s_idx.pop()
            s_idx.append(i)    

        return res
