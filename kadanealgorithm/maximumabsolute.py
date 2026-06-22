class Solution(object):
    def maxAbsoluteSum(self, nums):

        best_ending_positive = nums[0]
        best_ending_negative = nums[0]

        result_positive = nums[0]
        result_negative = nums[0]

        for i in range(1, len(nums)):

            # Maximum subarray sum
            if best_ending_positive + nums[i] < nums[i]:
                best_ending_positive = nums[i]
            else:
                best_ending_positive = best_ending_positive + nums[i]

            result_positive = max(result_positive, best_ending_positive)

            # Minimum subarray sum
            if best_ending_negative + nums[i] > nums[i]:
                best_ending_negative = nums[i]
            else:
                best_ending_negative = best_ending_negative + nums[i]

            result_negative = min(result_negative, best_ending_negative)

        return max(abs(result_positive), abs(result_negative))
#Example usage:
solution = Solution()
print(solution.maxAbsoluteSum([1, -3, 2, 3, -4]))  # Output: 5