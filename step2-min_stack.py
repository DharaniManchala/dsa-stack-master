"""
📌 Problem: Min Stack (LeetCode #155)
-------------------------------------

🧠 Design a stack that supports:
- push(x)
- pop()
- top()
- getMin() — all in O(1) time

📈 Time Complexity:
- push: O(1)
- pop: O(1)
- top: O(1)
- getMin: O(1)

📦 Space Complexity:
- O(n)

🛠️ Approach:
Use two stacks:
1. main_stack: to store all elements
2. min_stack: to store current minimums
"""
class MinStack:
    def __init__(self):
        self.stack=[]
        self.minstack=[]
    def push(self,x):
        self.stack.append(x) 
        if not self.minstack or x<=self.minstack[-1]:
            self.minstack.append(x)
    def pop(self):
        if self.stack:
            popped=self.stack.pop()
            if self.minstack and popped==self.minstack[-1]:
                self.minstack.pop()
    def top(self):
        if self.stack:
            return self.stack[-1]
        return "stack is underflow"
    def getmin(self):
        if self.minstack:
            return self.minstack[-1]
        return "stack is underflow"
if __name__=="__main__":
    s=MinStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    print(s.getmin())       # 1
    s.pop()
    print(s.getmin())       # 1
    print(s.top())          # 4
    s.pop()
    print(s.getmin())       # 1
    s.pop()
    print(s.getmin())       # 1

    


