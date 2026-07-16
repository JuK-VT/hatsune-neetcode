class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)

        fleets = 1
        p_ttt = (target - pairs[0][0]) / pairs[0][1]

        for pair in pairs[1:]:
            ttt = (target - pair[0]) / pair[1]
            if ttt > p_ttt:
                fleets += 1
                p_ttt = ttt

        return fleets
        