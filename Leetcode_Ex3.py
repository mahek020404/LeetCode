#SORT LIST
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        h,hn = head,head.next
        while hn and hn.next:
            h = h.next
            hn =hn.next.next
        mid = h.next
        h.next = []
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left,right)

    def merge(self,l1,l2):
        a = ListNode()
        current = a
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 if l1 else l2
        return a.next

def linkedlist(arr):
    if not arr:
        return []
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linkedlist_list(head):
    r = []
    while head:
        r.append(head.val)
        head = head.next
    return r
solution = Solution()

#Example1
head = linkedlist([4,2,1,3])
sorted_head = solution.sortList(head)
print(linkedlist_list(sorted_head))
#Example2
head = linkedlist([-1,5,3,4,0])
sorted_head = solution.sortList(head)
print(linkedlist_list(sorted_head))
#Example3
head = linkedlist([])
sorted_head = solution.sortList(head)
print(linkedlist_list(sorted_head))