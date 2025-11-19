#include <unordered_map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        /**
         * Time Complexity: O(n) for iterating through array
         * Space Complexity: O(n) for creating the hashmap
         */
        std::unordered_map<int, int> num_count;
        for(int i = 0; i < nums.size(); i++){
            int goal = target - nums[i];
            if(num_count.contains(goal)){
                return {num_count[goal], i};
            } else {
                num_count.insert({nums[i], i});
            }
        }
        return {};
    }
};