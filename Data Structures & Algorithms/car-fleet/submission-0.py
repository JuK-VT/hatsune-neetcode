class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        s = []

        for p in pair:
            time = (target - p[0]) / p[1]

            if s and s[-1] < time:
                s.append(time)
            
            if not s:
                s.append(time)

        return len(s)
