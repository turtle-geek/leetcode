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
        int r = 0;
        int profit = 0;
        for(r = 0; r < prices.size(); r++){
            while(prices[l] > prices[r]){
                l++;
            }
            profit = std::max(profit, prices[r] - prices[l]);
        }
        return profit;
    }
};