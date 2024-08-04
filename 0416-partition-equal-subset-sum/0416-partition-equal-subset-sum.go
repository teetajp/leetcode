func canPartition(nums []int) bool {
    sum := 0
    for _, val := range nums {
        sum += val
    }
    
    if sum % 2 != 0 {
        return false
    }
    
    target := sum / 2
    
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
    
    return false
}