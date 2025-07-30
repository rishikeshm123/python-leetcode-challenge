# 278 - First Bad Version
# Leetcode Link: https://leetcode.com/problems/first-bad-version/?envType=problem-list-v2&envId=binary-search

# This is a mock for demonstration. In the real interview, this function is already implemented.
def isBadVersion(version):
    return version >= 4  

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
    
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid  
            else:
                left = mid + 1
        
        return left
        
if __name__ == "__main__":
    sol = Solution()
    result = sol.firstBadVersion(n = 5)
    print('Result:',result)