class Solution:
    def nextsmaller(self,heights):
        stack=[]
        result=[-1]*len(heights)
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                result[i]=stack[-1]
            stack.append(i)
        return result
if __name__=="__main__":
    sol=Solution()
    print(sol.nextsmaller([2,1,5,6,2,3]))  # Output: [1, -1, 3, 4, 5, -1]
    print(sol.nextsmaller([2,4]))           # Output: [1, -1]
    print(sol.nextsmaller([1,1,1,1]))       # Output: [-1, -1, -1, -1]
    print(sol.nextsmaller([6,7,5,2,4,5]))   # Output: [3, 2, 3, -1, 5, -1]
# time complexity: O(n)
# space complexity: O(n)