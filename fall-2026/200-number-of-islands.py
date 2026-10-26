class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def bfs(m, n):
            if 0 <= m < len(grid) and 0 <= n < len(grid[0]) and grid[m][n] == "1":
                grid[m][n] = "0"
            else:
                return
            bfs(m-1,n)
            bfs(m+1,n)
            bfs(m,n-1)
            bfs(m,n+1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(i,j)
                    count += 1
        return count
