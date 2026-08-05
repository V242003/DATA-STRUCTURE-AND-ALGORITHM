class Solution:
    def findCeil(self, arr, x):
        low=0
        high=len(arr)-1
        result=-1
        while low<=high:
            guess=(low+high)//2
            if arr[guess]<x:
                low=guess+1
            else:
                if arr[guess]>=x:
                    result=guess
                    high=guess-1
        return result
# EXAMPLE USAGE
solution = Solution()
arr=[1, 2, 8, 10, 10, 12, 19]
x=5                                 
print(solution.findCeil(arr, x))  # Output: 2
        
