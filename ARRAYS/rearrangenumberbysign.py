class Solution(object):
    def rearrangeArray(self, nums):
        pos = []
        neg = []
        new_array = []

        for i in range(len(nums)):
            if nums[i] >= 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])

        i = 0
        j = 0

        while i < len(pos) and j < len(neg):
            new_array.append(pos[i])
            new_array.append(neg[j])

            i += 1
            j += 1

        return new_array
# example usage
nums=[3, 1, -2, -5, 2, -4]
solution = Solution()
result = solution.rearrangeArray(nums)
print(result)