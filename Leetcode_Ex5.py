#CONVERT SORTED ARRAY TO BINARY SEARCH TREE
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return None    
        mid = len(nums) // 2
        root = TreeNode(nums[mid])      
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])      
        return root
    def level_order_traversal(self, root):
        if not root:
            return []    
        result = []
        queue = [root]   
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)    
        while result and result[-1] is None:
            result.pop()     
        return result
s = Solution()
# Example 1
nums1 = [-10, -3, 0, 5, 9]
root1 = s.sortedArrayToBST(nums1)
print(s.level_order_traversal(root1))  
# Example 2
nums2 = [1, 3]
root2 = s.sortedArrayToBST(nums2)
print(s.level_order_traversal(root2))  