class Solution {
public:
    int singleNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        
        if (nums.size() == 1)
            return nums[0];
        
        for (int i = 1; i < nums.size(); i += 2) {
            if (nums[i-1] != nums[i]) {
                return nums[i-1];
            }        
        }
        
        return nums[nums.size()-1];
    }
};