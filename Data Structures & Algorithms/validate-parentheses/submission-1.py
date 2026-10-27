class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        closeToOpen = {")" : "(", "]" : "[", "}" : "{" } #mapping close to open parentheses; keys(Closing) : value(opening)

        for c in s: #going through every character
            if c in closeToOpen: #check if character is a closing parentheses by seeing if it is in closeToOpen, if it is then it is a closing parentheses
                if stack and stack[-1] == closeToOpen[c]: #passing in the closing parentheses and getting the open one #if closing parentheses make sure our stack is not empty, because we cannot add closing parentheses to empty stack and the top of the stack should be a matching open parentheses. 
                    stack.pop() #if matches then pop from the stack
                else:
                    return False #if parentheses dont match or is empty, then return false 
            else:
                stack.append(c) #if we get a open parentheses then we can add many as we want. take the character and append to our stack. example: "({[...""       
        return True if not stack else False #In the end after going through every character, only return true if stack is empty otherwise return false. Stack should be e,pty because we pop out every matching character
        