#BEAUTIFUL ARRAY
class Solution(object):
    def beautifulArray(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 1:
            return [1]
        result = []
        odds = self.beautifulArray((n + 1) // 2) 
        evens = self.beautifulArray(n // 2)  
        for x in odds:
            result.append(2 * x - 1)  
        for x in evens:
            result.append(2 * x)     
        return result
s = Solution()
#Example1
n = 4
print(s.beautifulArray(n)) 
#Example2
n = 5
print(s.beautifulArray(n)) 