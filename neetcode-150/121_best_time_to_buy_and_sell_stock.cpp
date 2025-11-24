#include <vector>
#include <algorithm>

class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        /**
         * Time complexity: O(n) for iterating through array
         * Space complexity: O(1) for using constant # of variables
         */
        int l = 0;
        int profit = 0;

        for(int r = 1; r < prices.size(); r++){
            if(prices[l] > prices[r]){
                l = r;
            }
            profit = std::max(profit, prices[r] - prices[l]);
        }
        return profit;
    }
};