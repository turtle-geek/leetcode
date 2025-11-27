#include <vector>

class Solution {

private:
    void dfs(std::vector<std::vector<int>>& image, int sr, int sc, int original_color, int color){
        // check valid color and valid range in image
        if(sr < 0 || sr >= image.size() || sc < 0 || sc >= image[0].size()){
            return;
        }

        // Ensure that you are checking array values within the bounds before checking below
        if(image[sr][sc] != original_color){
            return;
        }
        
        // changes if passes all checks
        image[sr][sc] = color;
        
        // dfs traversal
        dfs(image, sr + 1, sc, original_color, color);
        dfs(image, sr - 1, sc, original_color, color);
        dfs(image, sr, sc + 1, original_color, color);
        dfs(image, sr, sc - 1, original_color, color);
    }

public:
    std::vector<std::vector<int>> floodFill(std::vector<std::vector<int>>& image, int sr, int sc, int color) {
        /**
         * Time Complexity: O(R*C) where R is the rows and C is the colums
         * Space Complexity: O(R*C) for the worst case recursive call stack depth
         */
        
        int original_color = image[sr][sc];

        // case where starting pixel is already the target color, no need to flood fill
        if(original_color == color){
            return image;
        }
        
        dfs(image, sr, sc, original_color, color);
        return image;
    }
};