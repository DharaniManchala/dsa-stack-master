"""
📌 Problem: Largest Rectangle in Histogram
🔗 Link: https://leetcode.com/problems/largest-rectangle-in-histogram/

🧠 Approach:
- Use a **monotonic increasing stack** to find the largest rectangle.
- Append sentinel values (0 at beginning and end) to handle boundaries easily.
- Iterate through each bar:
    - If current height is greater than or equal to the height at top of stack, push index.
    - If current height is less, pop from stack and calculate area with popped height.
    - Width is calculated as the distance between current index and new top of stack after popping.
- Keep track of the maximum area seen so far.

⏰ Time Complexity: O(n)
- Each bar is pushed and popped at most once.

💾 Space Complexity: O(n)
- Stack can hold at most all indices.
"""
class Solution:
    def largestReactangle(self,heights):
        heights=[0]+heights+[0]
        stack=[]
        max_area=0
        for i in range(len(heights)):
            while stack and heights[i]<heights[stack[-1]]:
                h=heights[stack.pop()]
                w=i-stack[-1]-1
                area=h*w
                max_area=max(max_area,area)
            stack.append(i)
        return max_area
if __name__=="__main__":
    sol=Solution()
    print(sol.largestReactangle([2,1,5,6,2,3]))  # Output: 10
    print(sol.largestReactangle([2,4]))           # Output: 4
    print(sol.largestReactangle([1,1,1,1]))       # Output: 4
    print(sol.largestReactangle([6,7,5,2,4,5]))   # Output: 12

