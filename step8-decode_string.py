"""
LeetCode 394: Decode String
---------------------------

🔗 Problem Link:
https://leetcode.com/problems/decode-string/

📝 Problem:
Given an encoded string, return its decoded version.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets
is repeated exactly k times. k is guaranteed to be a positive integer.

You may assume that the input string is always valid — no extra whitespaces, well-formed brackets, etc.

Examples:
---------
Input:  s = "3[a]2[bc]"
Output: "aaabcbc"

Input:  s = "3[a2[c]]"
Output: "accaccacc"

💡 Approach:
We use a *stack* to decode the string from left to right.

- If we find a number → build the full number (could be multi-digit).
- If we find '[' → push the current string and count onto the stack.
- If we find ']' → pop from the stack and multiply the current string.
- If we find a character → add to current string.

This handles *nested encodings* elegantly using stack frames.

⏱ Time Complexity: O(n)
Each character is processed once. String multiplication and concatenation are also O(n) total.

📦 Space Complexity: O(n)
We use a stack to store intermediate strings and counts. In the worst case (deeply nested),
this could require O(n) additional space.
"""
def decodestr(str):
    stack=[]
    curr_num=0
    curr_str=""
    for char in str:
        if char.isdigit():
            curr_num=curr_num*10+int(char)
        elif char=='[':
            stack.append((curr_str,curr_num))
            curr_str=""
            curr_num=0
        elif char==']':
            prev_str,num=stack.pop()
            curr_str=prev_str+curr_str*num
        else:
            curr_str+=char
    return curr_str
if __name__=="__main__":
    print(decodestr("3[a]2[bc]"))          # Output: "aaabcbc"
    print(decodestr("3[a2[c]]"))           # Output: "accaccacc"
    print(decodestr("2[abc]3[cd]ef"))      # Output: "abcabccdcdcdef"
    print(decodestr("10[a]"))              # Output: "aaaaaaaaaa"

            
