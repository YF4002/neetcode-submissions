class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        nums_set = set(nums)
        ans = 1

        for num in nums_set:
            if num - 1 not in nums_set:
                curr = 1

                while num + curr in nums_set:
                    curr += 1
                
                ans = max(ans, curr)

        return ans
        