class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [-1] * len(height)
        max_right = [-1] * len(height)
        water = [-1] * len(height)

        max_l = 0
        max_r = 0
        for i in range(len(height)):
            max_left[i] = max_l
            if height[i] > max_l:
                max_l = height[i]
            max_right[-i - 1] = max_r
            if height[-i - 1] > max_r:
                max_r = height[-i - 1]

        print(max_left)
        print(max_right)

        for i in range(len(height)):
            water_col = min([max_left[i], max_right[i]]) - height[i]
            water[i] = max([water_col, 0])

        print(water)

        return sum(water)
        
        