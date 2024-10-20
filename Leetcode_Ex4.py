#MERGE TWO SORTED LIST
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 if list1 else list2
        return dummy.next
    @staticmethod
    def print_list(node):
        """
        Helper function to print the linked list.
        :param node: ListNode
        """
        result = []
        while node:
            result.append(node.val)
            node = node.next
        print(result)
s = Solution()
# Example 1
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
merged_list = s.mergeTwoLists(list1, list2)
s.print_list(merged_list)
# Example 2
list1 = None
list2 = None
merged_list = s.mergeTwoLists(list1, list2)
s.print_list(merged_list)
# Example 3
list1 = None
list2 = ListNode(0)
merged_list = s.mergeTwoLists(list1, list2)
s.print_list(merged_list)