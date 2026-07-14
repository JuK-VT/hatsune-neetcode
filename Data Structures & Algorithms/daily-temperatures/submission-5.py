class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s_temp = []
        s_idx = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            print(s_temp)
            if s_temp and temperatures[i] > s_temp[-1]:
                print(temperatures[i], s_temp[-1])
                while temperatures[i] > s_temp[-1]:
                    res[s_idx[-1]] = i - s_idx[-1]
                    s_temp.pop()
                    s_idx.pop()
                    if len(s_temp) == 0:
                        break
            s_temp.append(temperatures[i])
            s_idx.append(i)    

        return res
                

        