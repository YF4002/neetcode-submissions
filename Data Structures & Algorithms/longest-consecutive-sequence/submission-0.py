class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        nums = sorted(set(nums))
        ans = 1
        curr = 1

        for i in range(len(nums)- 1):
            if nums[i] + 1 == nums[i + 1]:
                curr += 1
                ans = max(ans, curr)
            else:
                curr = 1
        
        return ans
        