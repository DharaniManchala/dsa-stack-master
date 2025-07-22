"""
LeetCode 739: Daily Temperatures
---------------------------------

Given a list of daily temperatures, return a list such that, for each day,
tells you how many days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.

Example:
---------
Input:  temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]

Approach:
---------
We use a monotonic decreasing stack to keep track of indices whose temperatures
have not yet found a warmer day. For each temperature, we check if it's warmer 
than the temperature at the top index of the stack. If it is, we pop from the stack 
and calculate the number of days waited.

Time Complexity: O(n)
---------------------
Each element is pushed and popped from the stack at most once.

Space Complexity: O(n)
----------------------
We use a stack to store indices, which in the worst case could be all indices in the input.
"""
from typing import List
class Solution:
    def dailytemperatures(self,temperatures):
        n=len(temperatures)
        stack=[]
        result=[0]*n
        for i in range(n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev_index=stack.pop()
                result[prev_index]=i-prev_index
            stack.append(i)
        return result
if __name__=="__main__":
    s=Solution()
    print(s.dailytemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # Output: [1, 1, 4, 2, 1, 1, 0, 0]
    print(s.dailytemperatures([30, 40, 50, 60]))