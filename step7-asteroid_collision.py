"""
LeetCode 735: Asteroid Collision
--------------------------------

🔗 Problem Link:
https://leetcode.com/problems/asteroid-collision/

📝 Problem:
Given an array asteroids representing asteroids in a row. 
- The absolute value represents size.
- The sign represents direction:
    - Positive → right-moving
    - Negative → left-moving

All asteroids move at the same speed. When two asteroids meet:
- The smaller one explodes.
- If both are the same size, both explode.
- Asteroids moving in the same direction will never meet.

Return the state of the asteroids after all collisions.

Example:
---------
Input:  asteroids = [5, 10, -5]
Output: [5, 10]

Explanation:
10 and -5 collide → 10 survives, -5 explodes.

💡 Approach:
We use a stack to simulate asteroid movements and handle collisions:
- Push asteroid if:
    - Stack is empty
    - Asteroid is moving right
    - Top of stack is moving left
- If current asteroid is moving left and top is moving right:
    - Compare sizes:
        - If current is larger: pop top, repeat check
        - If equal: pop top, discard current
        - If smaller: discard current

⏱ Time Complexity: O(n)  
📦 Space Complexity: O(n)
"""

from typing import List
class Solution:
    def asteroid_collision(self,asteroids):
        stack=[]
        for ast in asteroids:
            while stack and ast<0<stack[-1]:
                if stack[-1]<-ast:
                    stack.pop()
                    continue
                elif stack[-1]==-ast:
                    stack.pop()
                break
            else:
                stack.append(ast)
        return stack
if __name__=="__main__":
    s=Solution()
    print(s.asteroid_collision([5,10,-5]))
    # Output: [5, 10]