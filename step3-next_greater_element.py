"""
🔹 Problem: Next Greater Element
Given an array, find the Next Greater Element (NGE) for every element.
The Next Greater Element for an element x is the first greater element
on the right side of x in the array. If no greater element exists, output -1.

📦 Time Complexity: O(n)
📦 Space Complexity: O(n)
💡 Approach: Monotonic Stack (Decreasing Stack)
"""
def next_greater_element(arr):
    stack=[]
    n=len(arr)
    result=[-1]*n
    for i in range(n):
        while stack and arr[i]>arr[stack[-1]]:

           index=stack.pop()
           result[index]=arr[i]
        stack.append(i)
    return result
if __name__=="__main__":
    arr=[4,5,2,10,8]
    print(next_greater_element(arr))  # Output: [5, 10, 10, -1, -1]
    arr=[1,3,2,4]
    print(next_greater_element(arr))  # Output: [3, 4, 4, -1]
    