# 📌 Problem: 239. Sliding Window Maximum

# 🔗 LeetCode: https://leetcode.com/problems/sliding-window-maximum/

# 🧠 Approach:

# - Use a deque to efficiently maintain a list of candidate maximum indices.
# - Remove indices that are:
#   - Outside the current sliding window
#   - Smaller than the current number (since they can't be the max anymore)
# - The front of the deque always holds the index of the maximum for the current window.
# - Append that maximum to the result once the first window is fully formed.

# ⏰ Time Complexity: O(n)
# - Each element is pushed and popped from the deque at most once.

# 💾 Space Complexity: O(k)
# - Deque holds at most k indices at any time

from collections import deque
def maximumslidingwindow(nums,k):
    n=len(nums)
    result=[]
    dq=deque()
    for i in range(n):
        if dq and dq[0]<=i-k:
            dq.popleft()
        while dq and nums[dq[-1]]<nums[i]:
            dq.pop()
        dq.append(i)
        if i>=k-1:
            result.append(nums[dq[0]])
    return result
if __name__=="__main__":
    print(maximumslidingwindow([1,3,-1,-3,5,3,6,7],3))  # Output: [3, 3, 5, 5, 6, 7]
    print(maximumslidingwindow([1],1))  # Output: [1]
    print(maximumslidingwindow([1,-1],1))  # Output: [1, -1]
    print(maximumslidingwindow([9,11],2))  # Output: [11]
    # time complexity: O(n)
    # space complexity: O(k)