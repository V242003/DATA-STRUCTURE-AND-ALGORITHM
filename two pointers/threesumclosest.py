class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()

        max_diff = float('inf')
        closest_sum = 0

        for i in range(len(nums) - 2):

            left = i + 1
            right = len(nums) - 1

            while left < right:

                sum = nums[i] + nums[left] + nums[right]
                difference = abs(sum - target)

                if difference < max_diff:
                    max_diff = difference
                    closest_sum = sum

                if sum == target:
                    return sum

                elif sum < target:
                    left += 1

                else:
                    right -= 1

        return closest_sum
# Example usage:
solution = Solution()
print(solution.threeSumClosest([-1, 2, 1, -4], 1))  # Output: 2