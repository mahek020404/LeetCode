#MAJORITY ELEMENTS
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate
# Example usage:
s = Solution()
#Example 1
print(s.majorityElement([3, 2, 3])) 
#Example 2
print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))  
