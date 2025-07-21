"""
🔹 Problem: Evaluate Reverse Polish Notation
📦 Time Complexity: O(n)
📦 Space Complexity: O(n)
💡 Approach: Use a stack to evaluate tokens
"""
class solution(object):
    def evalrpn(self,tokens):
        stack=[]
        for token in tokens:
            if token in ["+","-","*","/"]:
                b=stack.pop()
                a=stack.pop()
                if token=='+':
                    stack.append(a+b)
                elif token=='-':
                    stack.append(a-b)
                elif token=='*':
                    stack.append(a*b)
                elif token=='/':
                    stack.append(int(a/b))  # Use int() to truncate towards zero
            else:
                stack.append(int(token))
        return stack[0]
if __name__=="__main__":
    s=solution()
    print(s.evalrpn(["2","1","+"]))          # Output: 3
    print(s.evalrpn(["2","1","-"]))          # Output: 1