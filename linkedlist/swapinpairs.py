# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from middleelement import ListNode


class Solution(object):

    def reverse(self, head, size):
        prev = None
        curr = head

        while size > 0:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            size -= 1

        head.next = curr
        return prev

    def swapPairs(self, head):

        previousLeft = None
        left = head
        res = None
        size = 2

        while True:

            if left is None:
                break

            right = left

            for i in range(size - 1):
                if right is None:
                    break
                right = right.next

            if right:

                nextLeft = right.next

                right = self.reverse(left, size)

                if previousLeft:
                    previousLeft.next = right

                if res is None:
                    res = right

                previousLeft = left
                left = nextLeft

            else:

                if previousLeft:
                    previousLeft.next = left

                if res is None:
                    res = left

                break

        return res
# example usage
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    solution = Solution()
    new_head = solution.swapPairs(head)

    # Print the swapped linked list
    current = new_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")                                                                                                                                                   