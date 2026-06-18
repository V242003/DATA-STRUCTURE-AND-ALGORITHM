class Solution:
    def maxSubarraySum(self, arr, k):
        left=0
        right=k-1
        maximum=float('-inf')
        current_sum=0
        for i in range(left,right+1):
            current_sum+=arr[i]
                
        while right<len(arr):
            if current_sum>maximum:
                    maximum=current_sum
            left+=1
            right+=1
            current_sum=current_sum-arr[left-1]
            if right==len(arr):
                break
            else:
                current_sum+=arr[right]
        
        return maximum
# Example usage:
solution = Solution()
print(solution.maxSubarraySum([2, 1, 5, 1, 3, 2], 3))  # Output: 9