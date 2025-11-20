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
        int s_pos = 0;
        int t = 0;
        int max_len = 0;
        int curr_len = 0;

        while(t < s.length()){
            char curr_char = s[t];
            if(!seen_char.contains(curr_char)){
                seen_char.insert(curr_char);
                curr_len++;
            } else {
                if(curr_len > max_len){
                    max_len = curr_len;
                }
                while(s[s_pos] != curr_char){
                    seen_char.erase(s[s_pos]);
                    s_pos++;
                    curr_len--; // off by one
                }
                seen_char.erase(s[s_pos]);
                s_pos++;

                seen_char.insert(curr_char);
            }
            t++;
        }
        if(curr_len > max_len){
            max_len = curr_len;
        }
        return max_len;
    }
};