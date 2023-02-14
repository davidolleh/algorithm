class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def quickSort(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        start = head
        middle = self.findPivot(head=head)

        last = self.swapWithLastNode(head=start, middle=middle)

        right = last.prev
        left = head

        cnt = self.countNode(head=head)

        leftIdx = 0
        rightIdx = cnt - 1


        while leftIdx <= rightIdx:
            if left.val <= last.val:
                left = left.next
                leftIdx += 1
                continue

            if right.val >= last.val:
                right = right.prev
                rightIdx -= 1
                continue

            if left.val > last.val and last.val >= right.val:
                left.val, right.val = right.val, left.val
                continue

        left = left.next
        left.val, last.val = last.val, left.val


        rightHead = left.next
        rightHead.prev = None
        left.next =None

        left.next = None
        left.prev = None

        sortedRightHead = self.quickSort(head=rightHead)
        sortedLeftHead = self.quickSort(head=head)

        sortedLeftLast = sortedLeftHead

        while sortedLeftLast.next:
            sortedLeftLast = sortedLeftLast.next


        left.next = sortedRightHead
        sortedRightHead.prev = left
        left.prev = sortedLeftLast
        sortedLeftLast.next = left

        return sortedLeftHead


    def countNode(self, head:ListNode):
        cnt = 0
        while head.next:
            head= head.next
            cnt += 1

        return cnt




    def swapWithLastNode(self, head: ListNode, middle: ListNode):

        while head.next:
            head = head.next

        head.val, middle.val = middle.val, head.val

        return  head


    def findPivot(self, head: ListNode)-> ListNode:
        if not head or not head.next:
            return head

        slow = head
        fast = head.next

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow





l4 = ListNode(val=3)
l3 = ListNode(val=1, next=l4)
l2 = ListNode(val=2, next=l3)
l1 = ListNode(val=4, next= l2)

l4.prev=l3
l3.prev=l2
l2.prev=l1


s = Solution()
a = s.quickSort(head=l1)

print(a)