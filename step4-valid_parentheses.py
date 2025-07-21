"""
🔹 Problem: Valid Parentheses
Check if the input string of brackets is valid or not.

📦 Time Complexity: O(n)
📦 Space Complexity: O(n)
💡 Approach: Use Stack to match opening and closing brackets
"""

class Solution(object):
    def is_valid(self,s):
        stack=[]
        mapping={")":"(","]":"[","}":"{"}
        for char in s:
            if char in mapping:
                top_element=stack.pop() if stack else '#'
                if mapping[char]!=top_element:
                    return False
            else:
                stack.append(char)
        return not stack
if __name__=="__main__":
    s=Solution()
    print(s.is_valid("()"))
    print(s.is_valid("()[]{}"))
    print(s.is_valid("(]"))


             