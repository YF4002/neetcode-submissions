class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        new = [0] * len(nums)

        for i in range(len(nums) -1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1

            else:
                square = nums[left]
                left += 1
            
            new[i] = square * square
        
        return new