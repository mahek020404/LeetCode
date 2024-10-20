#LARGEST NUMBER
from functools import cmp_to_key
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums_str = list(map(str, nums))
        def compare(x, y):
            if x + y > y + x:
                return -1  
            else:
                return 1   
        nums_str.sort(key=cmp_to_key(compare))
        if nums_str[0] == "0":
            return "0"
        return ''.join(nums_str)
s = Solution()
#Example 1
print(s.largestNumber([10, 2]))  
#Example 2
print(s.largestNumber([3, 30, 34, 5, 9]))