# 744. Find Smallest Letter Greater Than Target
# Leetcode link: https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
# 

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left, right = 0, len(letters)
    
        # Use binary search to find the correct position
        while left < right:
            mid = left + (right - left) // 2
            
            # If the mid character is greater than the target, it could be a potential answer
            if letters[mid] > target:
                right = mid
            else:
                left = mid + 1
        
        # If 'left' is out of bounds, return the first character (circular condition)
        return letters[left % len(letters)]

            


if __name__ == '__main__':
    sol = Solution()
    test_case1 = sol.nextGreatestLetter(["c","f","j"],"a")
    print("Test Case 1:",test_case1)

    test_case2 = sol.nextGreatestLetter(["c","f","j"],"c")
    print("Test Case 2:",test_case2)

    test_case3 = sol.nextGreatestLetter(["x","x","y","y"],"z")
    print("Test Case 3:",test_case3)

    test_case4 = sol.nextGreatestLetter(["c","f","j"],"j")
    print("Test Case 4:",test_case4)



