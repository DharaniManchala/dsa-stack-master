"""✅ Problem Statement: Celebrity Problem
You're given a matrix M of size n x n such that M[i][j] = 1 means person i knows person j, and 0 means person i doesn't know person j.
A celebrity is someone who is known by everyone but knows no one.

🧠 Conditions for Celebrity:
M[celebrity][j] == 0 for all j ≠ celebrity → Celebrity knows no one.

M[i][celebrity] == 1 for all i ≠ celebrity → Everyone knows the celebrity.

✅ 👨‍💻 Naive Approach
🧠 Logic:
For each person, check both:

Does this person know anyone? (row check)

Is this person known by everyone? (column check)

⏱️ Time Complexity: O(n²)
🧠 Space Complexity: O(1)"""


# naive approach
def find_celebrity(M,n):
    for i in range(n):
        knows_someone=False
        konwn_by_all=True
        for j in range(n):
            if i!=j:
                if M[i][j]==1:
                    knows_someone=True
                if M[j][i]==0:
                    known_by_all=False
        if not knows_someone and known_by_all:

            
            return i
    return -1
if __name__=="__main__":
    M=[[0,1,0],[0,0,0],[1,1,0]]
    n=len(M)
    celebrity=find_celebrity(M,n)
    if celebrity!=-1:
        print(f"Celebrity is person {celebrity}")
    else:
        print("No celebrity found")
    
    M=[[0,1,0],[1,0,1],[1,1,0]]
    n=len(M)
    celebrity=find_celebrity(M,n)
    if celebrity!=-1:
        print(f"Celebrity is person {celebrity}")
    else:
        print("No celebrity found")
# time complexity: O(n^2)
# space complexity: O(1)

# ✅ 👨‍💻 Optimized Approach twopointers approach
def findcelebrity(M,n):
    celeb=0
    for i in range(1,n):
        if M[celeb][i]==1:
            celab=i
    for i in range(n):
        if i!=celeb:
            if M[celeb][i]==1 or M[i][celeb]==0:
                return -1
    return celeb
if __name__=="__main__":
    M=[[0,1,0],[0,0,0],[1,1,0]]
    n=len(M)
    celebrity=findcelebrity(M,n)
    if celebrity!=-1:
        print(f"Celebrity is person {celebrity}")
    else:
        print("No celebrity found")
    
    M=[[0,1,0],[1,0,1],[1,1,0]]
    n=len(M)
    celebrity=findcelebrity(M,n)
    if celebrity!=-1:
        print(f"Celebrity is person {celebrity}")
    else:
        print("No celebrity found")


# ⏱️ Time Complexity: O(n)
# - Each person is checked once.
# 🧠 Space Complexity: O(1)
    

# by stack approach
def find_celebrity(M,n):
    stack=[]
    for i in range(n):
        stack.append(i)
    while len(stack)>1:
        A=stack.pop()
        B=stack.pop()
        if M[A][B]==1:
            stack.append(B)
        else:
            stack.append(A)
    celebrity=stack.pop()
    for i in range(n):
        if i!=celebrity:
            if M[celebrity][i]==1 or M[i][celebrity]==0:
                return -1
    return celebrity
if __name__=="__main__":
    M=[[0,1,0],[0,0,0],[1,1,0]]
    n=len(M)
    celebrity=find_celebrity(M,n)
    if celebrity!=-1:
        print(f"Celebrity is person {celebrity}")
    else:
        print("No celebrity found")
    
    M=[[0,1,0],[1,0,1],[1,1,0]]
    n=len(M)
    celebrity=find_celebrity(M,n)
    if celebrity!=-1:
        print(f"Celebrity is person {celebrity}")
    else:
        print("No celebrity found")
# ⏱️ Time Complexity: O(n)
# - Each person is checked once.
# 🧠 Space Complexity: O(n)


