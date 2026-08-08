class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 2:
            return min(heights)

        max_product = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            max_product = max(min(heights[j], heights[i])*(j-i), max_product)
            if heights[j] < heights[i]:
                j -= 1
            else:
                i += 1
        return max_product