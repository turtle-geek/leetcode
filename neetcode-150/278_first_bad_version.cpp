// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        /**
         * Time Complexity: O(log(n)) for binary search
         * Space Complexity: O(1) for fixed number of variables
         */
        int l = 1;
        int r = n;
        int mid;
        while(l < r){
            mid = l + (r - l)/2;
            if(isBadVersion(mid)){
                r = mid; //preserve this value 
            } else {
                l = mid + 1; // remove the value that isn't bad
            }
        }
        return l; // l == r when the loop terminates
    }
};