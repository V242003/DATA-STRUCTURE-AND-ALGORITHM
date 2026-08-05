class Solution(object):
    def search(self, nums, target):
        low=0
        high=len(nums)-1
        while low<=high:
            guess=(low+high)//2
            if nums[guess]==target:
                return guess
            else:
                if nums[guess]<target:
                    low=guess+1
                else:
                    high=guess-1
        return -1
# EXAMPLE USAGE
solution = Solution()
nums=[-1,0,3,5,9,12]
target=9
result = solution.search(nums, target)
print(result)  # Output: 4
