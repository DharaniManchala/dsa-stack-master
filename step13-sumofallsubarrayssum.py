class solution:
    def sumofallsubarraysums(self,arr):
        n=len(arr)
        totalsum=0
        for i in range(n):
            contribution=arr[i]*(i+1)*(n-i)
            totalsum+=contribution
        return totalsum
if __name__=="__main__":
    sol=solution()
    print(sol.sumofallsubarraysums([1,2,3]))  # Output: 20
    print(sol.sumofallsubarraysums([1,2,3,4]))  # Output: 50
    print(sol.sumofallsubarraysums([5,6,7]))  # Output: 126
    print(sol.sumofallsubarraysums([10,20,30,40]))  # Output: 500
    # time complexity: O(n)
    # space complexity: O(1)