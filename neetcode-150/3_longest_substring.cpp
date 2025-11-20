#include <unordered_set>
#include <string>

class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        /**
         * Time Complexity: O(n) for s_pos and t sliders
         * Space Complexity: O(n) for creating the hashset
         */

        std::unordered_set<int> seen_char;
        int l = 0;
        int r = 0;
        int max_len = 0;

        for(int r = 0; r < s.length(); r++){
            while(seen_char.contains(s[r])){
                seen_char.erase(s[l]);
                l++;
            }
            seen_char.insert(s[r]);
            int curr_len = r - l + 1;
            if(curr_len > max_len){
                max_len = curr_len;
            }
        }
        return max_len;
    }
};