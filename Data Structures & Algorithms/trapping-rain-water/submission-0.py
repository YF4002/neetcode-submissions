class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0
            
        res = 0

        l, r = 0, len(height) - 1

        max_L, max_R = height[l], height[r]

        while l < r:
            if max_L < max_R:
                l += 1
                max_L = max(max_L, height[l])
                res += max_L - height[l]
            else:
                r -= 1
                max_R = max(max_R, height[r])
                res += max_R - height[r]
        
        return res
        