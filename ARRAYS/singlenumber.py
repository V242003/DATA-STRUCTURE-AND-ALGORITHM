class Solution:
    def singleNumber(self, nums):
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        for num in hashmap:
            if hashmap[num] == 1:
                return num
# example usage
solution = Solution()
nums = [4, 1, 2, 1, 2]
print(solution.singleNumber(nums))  # Output: 4
