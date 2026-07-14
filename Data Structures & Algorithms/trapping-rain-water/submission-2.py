class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l = height[l]
        max_r = height[r]
        water = 0

        while l < r:
            if max_l < max_r:
                water += max([(max_l - height[l]), 0])
                l += 1
                if height[l] > max_l:
                    max_l = height[l]
            else:
                water += max([(max_r - height[r]), 0])
                r -= 1
                if height[r] > max_r:
                    max_r = height[r]

        return water
        