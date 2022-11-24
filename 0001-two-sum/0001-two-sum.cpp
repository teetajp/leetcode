class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> num_idx; // stores index of numbers, must be careful since default is 0 when undefined
        for (int i = 0; i < nums.size(); i++) {
            
            if (num_idx.find(target - nums[i]) != num_idx.end())
                return vector<int>{i, num_idx[target - nums[i]]};
            
            num_idx[nums[i]] = i;
        }
        return vector<int>{-1, -1}; // placeholder (should not reach here)
    }
};