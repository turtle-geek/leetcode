class Solution {
public:
    /**
     * Time Complexity: O(log(n)) for binary search
     * Space Complexity: O(1) for fixed number of variables
     */
    int search(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;

        while(low <= high){
            int mid = low + (high - low) / 2;

            if(nums[mid] == target){
                return mid;
            }
            if(nums[low] <= nums[mid]){
                if(target >= nums[low] && target < nums[mid]){
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            } else {
                if(target > nums[mid] && target <= nums[high]){
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
        }
        return -1;
    }
};