class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1)])

        if window_count == s1_count:
            return True

        for i in range(len(s1), len(s2)):
            # add new char entering window
            window_count[s2[i]] += 1
            # remove old char leaving window
            old_char = s2[i - len(s1)]
            window_count[old_char] -= 1
            if window_count[old_char] == 0:
                del window_count[old_char]
            
            if window_count == s1_count:
                return True
        return False