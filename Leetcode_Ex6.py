#SORT AN ARRAY
class Solution(object):
    def merge_sort(self, nums):
        """
        Sorts the input array using Merge Sort.
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left_half = self.merge_sort(nums[:mid])
        right_half = self.merge_sort(nums[mid:])
        return self.merge(left_half, right_half)
    def merge(self, left, right):
        sorted_array = []
        i = 0  
        j = 0 
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1
        while i < len(left):
            sorted_array.append(left[i])
            i += 1       
        while j < len(right):
            sorted_array.append(right[j])
            j += 1
        return sorted_array
    def sortArray(self, nums):
        return self.merge_sort(nums)
s = Solution()
# Example1
nums1 = [5, 2, 3, 1]
print(s.sortArray(nums1))
# Example2
nums2 = [5, 1, 1, 2, 0, 0]
print(s.sortArray(nums2))  