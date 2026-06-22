class Solution(object):
    def maxProduct(self, nums):
        best_mul = nums[0]      # current max
        min_mul = nums[0]       # current min
        max_mul = nums[0]       # answer

        for i in range(1, len(nums)):

            temp_best = max(
                nums[i],
                best_mul * nums[i],
                min_mul * nums[i]
            )

            min_mul = min(
                nums[i],
                best_mul * nums[i],
                min_mul * nums[i]
            )

            best_mul = temp_best

            max_mul = max(max_mul, best_mul)

        return max_mul
#Example usage:
solution = Solution()
print(solution.maxProduct([2,3,-2,4]))  # Output: 6