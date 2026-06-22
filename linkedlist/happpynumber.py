class Solution(object):
    def isHappy(self, n):

        def square(n):
            total = 0

            while n > 0:
                remainder = n % 10
                total += remainder ** 2
                n = n // 10

            return total

        slow = n
        fast = n

        while True:
            slow = square(slow)
            fast = square(square(fast))

            if slow == 1 or fast == 1:
                return True

            if slow == fast:
                return False

# example usage
solution = Solution()
print(solution.isHappy(19))  # Output: True