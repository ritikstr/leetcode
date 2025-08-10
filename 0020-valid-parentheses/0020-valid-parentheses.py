class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening brackets
        stack = []
        
        # Mapping of closing brackets to their corresponding opening brackets
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        # Iterate through each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop from stack if stack is not empty, otherwise assign a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped element matches the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push to the stack
                stack.append(char)
        
        # In the end, stack should be empty if all brackets are valid
        return not stack
