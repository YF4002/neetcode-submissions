class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l=r=0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            
            r += 1
        
        return output


        

#use k size of window to iterate through the arr
#create a ans=[] to input the max in each window
# create a case where if lenght of window == k then get the max element in that window
# if its more than k then left += 1 if its less than k then right -= 1