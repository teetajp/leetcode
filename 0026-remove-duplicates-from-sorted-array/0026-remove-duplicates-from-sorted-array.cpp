class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // Perform "Bubble Sort" with each distinct element bubbling to the front
        int l = 1; // left pointer to keep track of place to insert
        for (int r = 1; r < nums.size(); r++) {
            if (nums[r] != nums[r-1]) {
                nums[l++] = nums[r];
            }
        }
        return l;
    }
};