class Solution():
    def searchMatrix(self,matrix,target):
        m=len(matrix)
        n=len(matrix[0])
        low=0
        high=m*n-1
        while low<=high:
            guess=(low+high)//2
            row=guess//n
            col=guess%n
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                low=guess+1
            else:
                high=guess-1
        return False
# example usage
sol = Solution()
print(sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))