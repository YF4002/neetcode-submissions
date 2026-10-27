class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)) #output result to match the length of input nums

        prefix = 1 #initialize the prefix value to 1
        for i in range(len(nums)): #for each position in nums
            res[i] = prefix # for each position in result output array i, take prefix and puts in position i
            prefix *= nums[i] #take input array nums i, multiply with what the prefix happens to be
        postfix = 1 # initialize postfix value with 1
        for i in range(len(nums) -1, -1, -1): # start at the end of the input array to the beginning
            res[i] *= postfix # value already in result of i multiply with postfix
            postfix *=nums[i] # postfix multiply with input array nums
        return res #return output array result



        