class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // Perform "Bubble Sort" with each distinct element bubbling to the front
        int l = 1; // left pointer to keep track of place to insert
        int r = 1; // right pointer which checks for the next distinct element to move to front
        while (r < nums.size()) {
            if (nums[r] != nums[r-1]) {
                nums[l] = nums[r];
                l++;
            }
            r++;
        }
        return l;
    }
};