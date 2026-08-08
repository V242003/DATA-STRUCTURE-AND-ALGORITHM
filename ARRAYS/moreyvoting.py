class Solution:
    def majorityElement(self, nums):
        element = nums[0]
        count = 0

        for i in range(len(nums)):
            if count == 0:
                element = nums[i]
                count = 1

            elif nums[i] == element:
                count += 1

            else:
                count -= 1

        return element
# example usage
nums=  [3, 2, 3]
solution = Solution()
result = solution.majorityElement(nums)
print(result)  # Output: 3