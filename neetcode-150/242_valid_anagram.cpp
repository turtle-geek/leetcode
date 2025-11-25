#include <string>

class Solution {
public:
    bool isAnagram(std::string s, std::string t) {
        /**
         * Time Complexity: O(n) for iterating through string
         * Space Complexity: O(1) for creating alphabet indexing
         */
        if(s.length() != t.length()){
            return false;
        }
        int char_count[26] = {0};
        for(int i = 0; i < s.length(); i++){
            char_count[s[i]-'a']++;
            char_count[t[i]-'a']--;
        }

        for(int j : char_count){
            if(j != 0){
                return false;
            }
        }
        return true;
    }
};