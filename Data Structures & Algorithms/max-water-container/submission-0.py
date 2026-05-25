class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        for i in range(len(heights)):
            for j in range(1, len(heights)):
                if i == j:
                    continue
                width = j - i
                height = min(heights[i], heights[j])
                area = width * height
                max_water = max(max_water, area) 
        return max_water