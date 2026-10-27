class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" #encode list into a single string
        for s in strs: #go string by each, character a ta time
            res += str(len(s)) + "#" + s # length of the string, followed by the '#' and then by the string itself. 
        return res #return the result

    def decode(self, s: str) -> List[str]:
        res, i = [], 0   # res as a list of string, and pointer i to tell us the position of where we are at in input string.

        while i < len(s): #while i is still in bound and lower than the length of the string
            j = i # find the end of integer, find '#'
            while s[j] != "#": #while j is not equal to '#', meaning a integer character.
                j += 1 #increment j by one until we reach '#'
            length = int(s[i:j])  #once we get to '#', string from index i to index j but not including index j. Its a string so convert it to integer.
            res.append(s[j + 1 : j + 1 + length]) #gives us the enitre string and append to result
            i = j + 1 + length #update pointer i to start on next word.

        return res

                

