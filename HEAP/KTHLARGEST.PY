import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        min_heap = []

        for i in range(k):
            heapq.heappush(min_heap, nums[i])

        for i in range(k, len(nums)):
            if nums[i] <= min_heap[0]:
                continue

            heapq.heappop(min_heap)
            heapq.heappush(min_heap, nums[i])

        return min_heap[0]
# Example usage
nums = [3, 2, 1, 5, 6, 4]
k = 2
solution = Solution()
result = solution.findKthLargest(nums, k)
print(result)  # Output: 5