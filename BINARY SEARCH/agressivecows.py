class Solution:
    def aggressiveCows(self, arr, k):

        def fun(arr, k, guess):
            cows = 1
            pos = arr[0]

            for i in range(1, len(arr)):
                distance = arr[i] - pos

                if distance >= guess:
                    cows += 1
                    pos = arr[i]

            return cows >= k

        arr.sort()

        n = len(arr)
        low = 0
        high = arr[n - 1] - arr[0]

        result = -1

        while low <= high:
            guess = (low + high) // 2

            if fun(arr, k, guess):
                result = guess
                low = guess + 1
            else:
                high = guess - 1

        return result
# example usage
sol = Solution()
print(sol.aggressiveCows([1, 2, 8, 4, 9], 3))