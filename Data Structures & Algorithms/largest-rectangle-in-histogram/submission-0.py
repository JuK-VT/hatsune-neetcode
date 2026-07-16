class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                idx, h = stack.pop()
                max_area = max(max_area, h * (i - idx))
                start = idx
            stack.append((start, heights[i]))

        while stack:
            idx, h = stack.pop()
            max_area = max(max_area, h * (len(heights) - idx))

        return max_area
