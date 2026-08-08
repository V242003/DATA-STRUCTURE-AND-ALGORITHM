class Solution(object):
    def minEatingSpeed(self, piles, h):

        def fun(piles, speed):
            hour = 0

            for i in range(len(piles)):
                hour += (piles[i] + speed - 1) // speed

            return hour

        low = 1
        high = max(piles)
        result = -1

        while low <= high:
            guess = (low + high) // 2

            hour = fun(piles, guess)

            if hour > h:
                low = guess + 1
            else:
                result = guess
                high = guess - 1

        return result
# example usage 
piles = [3, 6, 7, 11]   
h = 8
solution = Solution()
result = solution.minEatingSpeed(piles, h)
print(result)  # Output: 4
