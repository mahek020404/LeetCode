#CONTAINS DUPLICATE
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()  
        for num in nums:
            if num in seen:
                return True  
            seen.add(num) 
        return False  
s = Solution()
# Example 1:
print(s.containsDuplicate([1, 2, 3, 1]))  
# Example 2:
print(s.containsDuplicate([1, 2, 3, 4]))  
# Example 3:
print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  
