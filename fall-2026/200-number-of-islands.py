class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # Time complexity: O(m*n) iterating through every element in the matrix
        # Memory: O(m*n) worst case entire grid is land
        def dfs(m, n):
            if not(0 <= m < len(grid) and 0 <= n < len(grid[0]) and grid[m][n] == "1"):
                return
            grid[m][n] = "0"
            dfs(m-1,n)
            dfs(m+1,n)
            dfs(m,n-1)
            dfs(m,n+1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count += 1
        return count
