import heapq

class Solution:
    def kthSmallest(self, arr, k):
        max_heap = []

        # First k elements
        for i in range(k):
            heapq.heappush(max_heap, -arr[i])

        # Remaining elements
        for i in range(k, len(arr)):
            if arr[i] >= -max_heap[0]:
                continue

            heapq.heappop(max_heap)
            heapq.heappush(max_heap, -arr[i])

        return -max_heap[0]
# Example usage
arr = [7, 10, 4, 3, 20, 15]
k = 3
solution = Solution()
result = solution.kthSmallest(arr, k)
print(result)  # Output: 7