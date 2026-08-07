class Solution(object):
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            guess = (low + high) // 2

            if nums[guess] == target:
                return guess

            if nums[guess] > nums[-1]:      

                if nums[guess] < target:
                    low = guess + 1
                else:
                    if target < nums[0]:
                        low = guess + 1     
                    else:
                        high = guess - 1

            else:                          

                if nums[guess] > target:
                    high = guess - 1
                else:
                    if target > nums[-1]:
                        high = guess - 1
                    else:
                        low = guess + 1

        return -1
# example usage
solution=Solution()
nums=[4,5,6,7,0,1,2]
target=0
result=solution.search(nums,target)
print(result)  # Output: 4