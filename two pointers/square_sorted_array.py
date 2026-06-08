class Solution(object):
    def sortedSquares(self, nums):
        neg = []
        pos = []

        for n in nums:
            if n < 0:
                neg.append(n)
            else:
                pos.append(n)

        square_neg = [x**2 for x in neg]
        square_pos = [x**2 for x in pos]

        square_neg.sort()   

        result = []

        i = 0
        j = 0

        while i < len(square_neg) and j < len(square_pos):
            if square_neg[i] < square_pos[j]:
                result.append(square_neg[i])
                i += 1
            else:
                result.append(square_pos[j])
                j += 1

        while i < len(square_neg):
            result.append(square_neg[i])
            i += 1

        while j < len(square_pos):
            result.append(square_pos[j])
            j += 1

        return result

nums = [-4, -1, 0, 3, 10]
solution = Solution()
print(solution.sortedSquares(nums))