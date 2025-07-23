class Solution:
    def removekdigits(self,nums,k):
        stack=[]
        for num in nums:
            while k>0 and stack and stack[-1]>num:
                stack.pop()
                k-=1
            stack.append(num)
        while k>0:
            stack.pop()
            k-=1
        return ''.join(stack).lstrip('0') 
        return result if result else "0"
if __name__=="__main__":
    sol=Solution()
    print(sol.removekdigits("1432219",3))  # Output: "1219"
    print(sol.removekdigits("10200",1))    # Output: "200"
    print(sol.removekdigits("10",2))       # Output: "0"
                
                # time complexity: O(n)
                # space complexity: O(n)