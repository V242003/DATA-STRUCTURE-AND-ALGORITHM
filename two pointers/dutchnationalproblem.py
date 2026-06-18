class Solution(object):
    def sortColors(self, nums):
       low=0
       high=len(nums)-1
       mid=0
       while mid<=high:
            if nums[mid]==2:
                nums[mid],nums[high]=nums[high],nums[mid]
                high=high-1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[low]=nums[low],nums[mid]
                mid+=1
                low+=1
       return nums

# Example usage:
solution = Solution()
nums = [2, 0, 2, 1, 1, 0]
print(solution.sortColors(nums)) # Output: [0, 0, 1, 1, 2, 2]