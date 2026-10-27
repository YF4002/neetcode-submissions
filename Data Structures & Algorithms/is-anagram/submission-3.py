class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if len(sorted_s) != len(sorted_t):
            return False
 
        for i, j in zip(sorted_s, sorted_t):
            if i != j:
                return False
            
        return True

        