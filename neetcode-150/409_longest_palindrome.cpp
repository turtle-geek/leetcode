#include <unordered_map>
#include <string>

class Solution {
public:
    int longestPalindrome(std::string s) {
        /**
         * Time Complexity: O(n) for iterating through the string
         * Space Complexity: O(n) for declaring the hashmap
         */
        std::unordered_map<char, int> char_count;

        int len = 0;

        for(int i = 0; i < s.length(); i++){
            char_count[s[i]]++;
            if(char_count[s[i]] % 2 == 0){
                len += 2;
            }
        }

        for(const auto& pair : char_count){
            if(pair.second % 2 == 1){
                len++;
                break;
            }
        }

        return len;
    }
};