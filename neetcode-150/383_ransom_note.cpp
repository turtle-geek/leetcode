#include <string>

class Solution {
public:
    bool canConstruct(std::string ransomNote, std::string magazine) {
        /**
         * Time Complexity: O(n) for iterating through ransom and magazine
         * Space Complexity: O(1) for fixed number of variables (no hashmap)
         */
        if(ransomNote.length() > magazine.length()){
            return false;
        }

        int char_count[26] = {0};

        for(char m_char : magazine){
            char_count[m_char - 'a']++;
        }

        for(char r_char : ransomNote){
            int index = r_char - 'a';
            char_count[index]--;

            if(char_count[index] < 0){
                return false;
            }
        }
        return true;
    }
};