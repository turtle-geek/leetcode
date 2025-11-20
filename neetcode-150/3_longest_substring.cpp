#include <unordered_set>
#include <string>

class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        /**
         * Time Complexity: O(n) for left and right sliders
         * Space Complexity: O(n) for creating the hashset
         */

        std::unordered_set<int> seen_char;
        int left = 0;
        int right = 0;
        int max_len = 0;
        int curr_len = 0;

        while(right < s.length()){
            char curr_char = s[right];
            if(!seen_char.contains(curr_char)){
                seen_char.insert(curr_char);
                curr_len++;
            } else {
                if(curr_len > max_len){
                    max_len = curr_len;
                }
                while(s[left] != curr_char){
                    seen_char.erase(s[left]);
                    left++;
                    curr_len--; // off by one
                }
                seen_char.erase(s[left]);
                left++;

                seen_char.insert(curr_char);
            }
            right++;
        }
        if(curr_len > max_len){
            max_len = curr_len;
        }
        return max_len;
    }
};