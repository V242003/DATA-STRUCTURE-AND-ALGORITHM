class Solution:
    def pascalTriangleI(self, r, c):

        def funNcR(n, r):
            res = 1
            for i in range(r):
                res = res * (n - i)
                res = res // (i + 1)
            return res

        return funNcR(r - 1, c - 1)
# example usage
r = 4
c = 2
solution = Solution()
result = solution.pascalTriangleI(r, c)
print(result)  # Output: 3