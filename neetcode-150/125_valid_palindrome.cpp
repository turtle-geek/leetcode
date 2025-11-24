#include <string>

class Solution {
public:
    bool isPalindrome(std::string s) {
        /**
         * Time Complexity: O(n) for iterating through string
         * Space Complexity: O(n) for clean_string variable
         */

        std::string clean_string = "";
        
        for(char ch : s){
            if(std::isalnum(static_cast<unsigned char>(ch))){
                clean_string += static_cast<char>(
                    std::tolower(static_cast<unsigned char>(ch)));
            }
        }

        int l = 0;
        int r = clean_string.length() - 1;
        while(l < r){
            if(clean_string[l] != clean_string[r]){
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
};