class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int, bool> values_seen;
        for (auto val : nums) {
            if (values_seen[val] == true) {
                return true;
            }
            values_seen[val] = true;
        }
        return false;
    }
};