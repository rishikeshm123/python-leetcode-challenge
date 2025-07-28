# 1351. Count Negative Numbers in a Sorted Matrix
# leetcode link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/
# Solved using Binary Search

class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        total_negatives = 0
        for row in grid:
            left , right = 0, len(row)
            
            while left < right:
                mid = (left + right) //2
                if row[mid] < 0:
                    right = mid 
                else:
                    left = mid + 1

            total_negatives += (len(row) - left)

        return total_negatives

if __name__ == "__main__":
    grid = [[4,3,2,-1],
            [3,2,1,-1],
            [1,1,-1,-2],
            [-1,-1,-2,-3]]
    
    sol = Solution()
    result = sol.countNegatives(grid)
    print(result)