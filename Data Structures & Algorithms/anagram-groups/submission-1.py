class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping charCount : List of anagrams

        for word in strs:
            count = [0] * 26 # counting from a - z
            
            for c in word:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(word)

        return list(res.values())

        