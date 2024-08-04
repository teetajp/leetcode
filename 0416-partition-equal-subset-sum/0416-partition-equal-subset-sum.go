func canPartition(nums []int) bool {
    sum := 0
    
    for _, val := range nums {
        sum += val
    }
    
    target := sum / 2

    if (sum % 2 != 0) || (len(nums) == 1 && nums[0] != 0) {
        return false
    } else if target == 0 {
        return true
    }
    
    
    dp := make([]bool, target + 1)
    dp[0] = true
    
    for _, val := range nums {
        for i := target; i >= val; i-- {
            dp[i] = dp[i] || dp[i - val]
        }
        
        if dp[target] {
            return true
        }
    }
    
    return dp[target]
}