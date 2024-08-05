class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = 0;
        
        
        for (int num : nums) {
            sum += num;
        }
        
        if (sum % 2 != 0) return false;
        
        size_t n = nums.size();
        int target = sum / 2;
        
        vector<bool> dp(target+1, false);
        dp[0] = true;
        
        for (int num : nums) {
            for (int i = target; i >= num; i--) {
                dp[i] = dp[i] || dp[i - num];
            }
            
            if (dp[target]) {
                return true;
            }
        }
        
        
        return false;
    }
};