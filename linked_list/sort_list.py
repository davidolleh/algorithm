class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        return self.merge_sort(head=head)

    def merge_sort(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        middlePivot = self.findPivot(head=head)
        right = self.merge_sort(head=middlePivot.next)

        middlePivot.next = None

        left = self.merge_sort(head=head)

        return self.merge(l1=left, l2=right)

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(val=-1000)
        l3 = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next

            l3 = l3.next

        while l1:
            l3.next = l1
            l1 = l1.next
            l3 = l3.next

        while l2:
            l3.next = l2
            l2 = l2.next
            l3 = l3.next

        return dummy.next

    def findPivot(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        slow: ListNode = head
        fast: ListNode = head.next

        while fast.next and fast.next.next:
            slow = slow.next

            fast = fast.next.next

        return slow

l5 = ListNode(val=0)
l4 = ListNode(val=4, next=l5)
l3 = ListNode(val=3, next=l4)
l2 = ListNode(val=5, next=l3)
l1 = ListNode(val=-1, next= l2)

# l4 = ListNode(val=3)
# l3 = ListNode(val=1, next=l4)
# l2 = ListNode(val=2, next=l3)
# l1 = ListNode(val=4, next= l2)
s = Solution()
a = s.sortList(head=l1)

while a:
    print(a.val)
    a = a.next
