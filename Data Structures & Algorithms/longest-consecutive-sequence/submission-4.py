class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        nums_set= set(nums) #O(n) space
        ans = 0

        for num in nums_set: #O(n) loop
            if num-1 not in nums_set: #only start counting at beginning of sequence
                curr = 1
                while num + curr in nums_set: #if num and its next squence(num+curr) in nums_set then curr += 1
                    curr += 1
                
                ans = max(ans, curr)
        
        return ans

        