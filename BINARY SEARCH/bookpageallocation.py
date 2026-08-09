class Solution:
    def findPages(self, arr, k):

        def fun(arr, k, limit):
            students = 1
            pages = 0

            for i in range(len(arr)):
                if pages + arr[i] <= limit:
                    pages += arr[i]
                else:
                    students += 1
                    pages = arr[i]

                    if students > k:
                        return False

            return True

        n = len(arr)

        if n < k:
            return -1

        low = max(arr)
        high = sum(arr)
        result = -1

        while low <= high:
            guess = (low + high) // 2

            if fun(arr, k, guess):
                result = guess
                high = guess - 1
            else:
                low = guess + 1

        return result
# example usage
sol = Solution()
print(sol.findPages([12, 34, 67, 90], 2))
