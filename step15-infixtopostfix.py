def precedence(op):
    if op=='^':
        return 3
    if op=='*' or op=='/':
        return 2
    if op=='+' or op=='-':
        return 1
    return 0
def infix_to_postfix(expression):
    stack=[]
    postfix=""
    for char in expression:
        if char.isalnum():
            postfix+=char
        elif char=="(":
            stack.append(char)
        elif char==")":
            while stack and stack[-1]!="(":
                postfix+=stack.pop()
            stack.pop()
        else:
            while stack and precedence(stack[-1])>=precedence(char):
                postfix+=stack.pop()
            stack.append(char)
    while stack:
        postfix+=stack.pop()

    return postfix
if __name__=="__main__":
    print(infix_to_postfix("a+b*(c^d-e)^(f+g*h)-i"))  # Output: "abcd^e-fgh*+i-+*"
    print(infix_to_postfix("A+B-C"))  # Output: "AB+C-"
    print(infix_to_postfix("(A+B)*C"))  # Output: "AB+C*"
    print(infix_to_postfix("A*(B+C)/D"))  # Output: "ABC+D*/"
    # time complexity: O(n)
    # space complexity: O(n)