class Solution {
public:
    /**
     * Time Complexity: O(m*n) where m is rows and n is columns
     * Space Complexity: O(m*n) queue size
     */
    int orangesRotting(vector<vector<int>>& grid) {
        if (grid.empty()) return 0;

        int rows = grid.size();
        int cols = grid[0].size();
        queue<pair<int, int>> q;
        int freshOranges = 0;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 2) {
                    q.push({i, j});
                } else if (grid[i][j] == 1) {
                    freshOranges++;
                }
            }
        }

        if (freshOranges == 0) return 0;

        int minutes = 0;
        int dr[] = {-1, 1, 0, 0};
        int dc[] = {0, 0, -1, 1};

        while (!q.empty()) {
            int size = q.size();
            bool rottedAnyInThisLevel = false;

            for (int i = 0; i < size; i++) {
                auto [currR, currC] = q.front();
                q.pop();

                for (int d = 0; d < 4; d++) {
                    int nr = currR + dr[d];
                    int nc = currC + dc[d];

                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2;
                        q.push({nr, nc});
                        freshOranges--;
                        rottedAnyInThisLevel = true;
                    }
                }
            }
            if (rottedAnyInThisLevel) minutes++;
        }
        return freshOranges == 0 ? minutes : -1;
    }
};