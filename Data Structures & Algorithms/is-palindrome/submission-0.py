class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) -1 #Create two pointer left and right, left at index 0 (Start) and right at the end of the string (Last)

        while l < r: #while left is less than right, pointers have not yet met each other in middle
            while l < r and not self.alphaNum(s[l]): #while its not alphanumerical, we want to increment/ move up the left pointer by 1 
                l += 1
            while r > l and not self.alphaNum(s[r]): #while its not alphanumerical, we want to decrement/ move down the right pointer by 1
                r -= 1

            # we have now filter out the non alphanumericals and have the alphanumericals with us

            if s[l].lower() != s[r].lower(): #if character on left not equal to character right then its not equal and return False
                return False

            l,r =  l + 1, r -1 #Update the left and right pointer, moving it to the next postion ro do the next position of the while loop.
        
        return True #Once entire loop finishes, we can tell its a palindrome so we return True


    def alphaNum(self,c): #Make sure the character is a alphaNumerical from the ASCII
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

    
    #Slightly less efficient. No extra memory needed.
        