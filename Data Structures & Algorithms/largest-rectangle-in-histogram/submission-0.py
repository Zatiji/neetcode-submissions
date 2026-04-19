class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [(0, 0)] # (idx, value)

        for idx, height in enumerate(heights):
            previous_idx, previous_height = stack[-1]
            idx_in_stack = idx

            while height < previous_height:
                area = (idx - previous_idx) * previous_height
                max_area = max(max_area, area)
                idx_in_stack = previous_idx
                stack.pop()
                previous_idx, previous_height = stack[-1]
                
            stack.append((idx_in_stack, height))
        
        size = len(heights)
        while stack:
            idx, height = stack[-1]
            area = (size - idx) * height
            max_area = max(max_area, area)
            stack.pop()

        return max_area


        