class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> num_idx; // stores index of numbers, must be careful since default is 0 when undefined
        for (int i = 0; i < nums.size(); i++) {
            unordered_map<int, int>::iterator diff_idx = num_idx.find(target - nums[i]);
            
            if (diff_idx != num_idx.end()) {
                return vector<int>{i, diff_idx->second};
            }
            num_idx[nums[i]] = i;
        }
        return vector<int>{-1, -1}; // placeholder (should not reach here)
    }
};