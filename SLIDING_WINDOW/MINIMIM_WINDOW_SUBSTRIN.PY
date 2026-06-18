class Solution(object):
    def minWindow(self, s, t):

        if len(t) > len(s):
            return ""

        hash_t = [0] * 256
        hash_s = [0] * 256

        for ch in t:
            hash_t[ord(ch)] += 1

        start = 0
        start_index = -1
        min_len = float('inf')
        count = 0

        for end in range(len(s)):

            hash_s[ord(s[end])] += 1

            if (hash_t[ord(s[end])] != 0 and
                hash_s[ord(s[end])] <= hash_t[ord(s[end])]):
                count += 1

            if count == len(t):

                while (hash_t[ord(s[start])] == 0 or
                       hash_s[ord(s[start])] > hash_t[ord(s[start])]):

                    if hash_s[ord(s[start])] > hash_t[ord(s[start])]:
                        hash_s[ord(s[start])] -= 1

                    start += 1

                window_len = end - start + 1

                if window_len < min_len:
                    min_len = window_len
                    start_index = start

        if start_index == -1:
            return ""

        return s[start_index:start_index + min_len]
# Example usage:
solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"