class Solution(object):
    def maximumSum(self, arr):
        nodelete = arr[0]
        onedelete = float('-inf')
        result = arr[0]

        for i in range(1, len(arr)):
            previousnodelete = nodelete
            previousonedelete = onedelete

            nodelete = max(previousnodelete + arr[i], arr[i])

            if previousonedelete == float('-inf'):
                v2 = arr[i]
            else:
                v2 = previousonedelete + arr[i]

            onedelete = max(v2, previousnodelete)

            result = max(result, nodelete, onedelete)

        return result
#Example usage:
solution = Solution()
print(solution.maximumSum([1,-2,0,3]))  # Output: 4
