#Merge Sorted Array
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        a = m-1
        b = n-1                               
        l = m+n-1
        while(b>=0):
            if (a>=0 and nums1[a] > nums2[b]):
                nums1[l] = nums1[a]
                l-=1
                a-=1
            else:
                nums1[l] = nums2[b]
                l-=1
                b-=1
if __name__ == '__main__':
    #Example1
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    s = Solution()
    s.merge(nums1, m, nums2, n) 
    print(nums1)
    #Example2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    s = Solution()
    s.merge(nums1, m, nums2, n)  
    print(nums1)
    #Example3
    num1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    s = Solution()
    s.merge(nums1, m, nums2, n) 
    print(nums1)    