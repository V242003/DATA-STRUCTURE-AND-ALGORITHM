class Solution(object):
    def peakIndexInMountainArray(self, arr):
        low=0
        result=-1
        high=len(arr)-1
        while low<=high:
            guess=(low+high)//2
            if arr[guess]<arr[guess+1]:
                low=low+1
            else:
                result=guess
                high=high-1
        return result
# example usage
arr=[0, 2, 1, 0]
solution = Solution()   
print(solution.peakIndexInMountainArray(arr))  # Output: 1      