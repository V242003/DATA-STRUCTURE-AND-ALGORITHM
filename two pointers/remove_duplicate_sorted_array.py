class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        j=1
        while j<len(nums):
                if nums[i]==nums[j]:
                    j=j+1
                else:
                    i=i+1
                    nums[i]=nums[j]
                    j=j+1
        return i+1
nums=[1,1,2]
solution=Solution()
print(solution.removeDuplicates(nums))