class Solution(object):
    def findMin(self, nums):
        low = 0
        high = len(nums) - 1
        result = nums[0]

        while low <= high:
            guess = (low + high) // 2

            if nums[guess] > nums[-1]:
                low = guess + 1
            else:
                result = nums[guess]
                high = guess - 1

        return result
# example usage
solution=Solution()
nums=[3,4,5,1,2]
print(solution.findMin(nums))  # Output: 1  