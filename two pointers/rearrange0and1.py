class Solution:
    def segregate0and1(self, arr):
        left=0
        right=len(arr)-1
        while left<right:
            if arr[left]==0:
                left=left+1
            elif arr[right]==1:
                right=right-1
            else:
                arr[left],arr[right]=arr[right],arr[left]
                left=left+1
                right=right-1
        return arr
    
arr=[0,1,0,1,0,1]
solution=Solution()
print(solution.segregate0and1(arr))