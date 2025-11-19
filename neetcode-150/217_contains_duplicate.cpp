#include <unordered_set>

class Solution {
public:
    bool containsDuplicate(std::vector<int>& nums) {
        /**
         * Time complexity: O(n) for traversing array
         * Space complexity: O(n) for creating hashset
         */
        std::unordered_set<int> seen;
        for(int num : nums){
            if(seen.count(num)){
                return true;
            } else {
                seen.insert(num);
            }
        }
        return false;
    }
};
