# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from cycledetection import ListNode


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

    def reverseKGroup(self, head, k):

        previousLeft = None
        left = head
        res = None

        while True:

            if left is None:
                break

            right = left

            # check if k nodes are available
            for i in range(k - 1):
                if right.next is None:
                    break
                right = right.next

            # less than k nodes left
            if right.next is None and k > 1:
                count = 1
                temp = left
                while temp.next:
                    temp = temp.next
                    count += 1

                if count < k:
                    if previousLeft:
                        previousLeft.next = left
                    if res is None:
                        res = left
                    break

            nextLeft = right.next

            right = self.reverse(left, k)

            if previousLeft:
                previousLeft.next = right

            if res is None:
                res = right

            previousLeft = left
            left = nextLeft

        return res
# example usage:
if __name__ == "__main__":
    
    # create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    k = 2

    solution = Solution()
    new_head = solution.reverseKGroup(head, k)

    # print the reversed linked list
    current = new_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")