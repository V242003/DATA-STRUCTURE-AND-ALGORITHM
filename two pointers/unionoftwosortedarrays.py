class Solution:
    def unionArray(self, nums1, nums2):
        union = []
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):

            if nums1[i] <= nums2[j]:
                if len(union) == 0 or union[-1] != nums1[i]:
                    union.append(nums1[i])
                i += 1
            else:
                if len(union) == 0 or union[-1] != nums2[j]:
                    union.append(nums2[j])
                j += 1

        while i < len(nums1):
            if len(union) == 0 or union[-1] != nums1[i]:
                union.append(nums1[i])
            i += 1

        while j < len(nums2):
            if len(union) == 0 or union[-1] != nums2[j]:
                union.append(nums2[j])
            j += 1

        return union
# # Example usage:
solution = Solution()
nums1 = [1, 2, 3, 4, 5]
nums2 = [3, 4, 5, 6, 7]
result = solution.unionArray(nums1, nums2)
print(result)  # Output: [1, 2, 3, 4, 5, 6, 7]      