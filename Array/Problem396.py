class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)
        
        total_sum = sum(nums)
        
        # Calculate F(0)
        f = sum(i * nums[i] for i in range(n))
        
        ans = f
        
        # Relation:
        # F(k) = F(k-1) + total_sum - n * nums[n-k]
        for k in range(1, n):
            f = f + total_sum - n * nums[n - k]
            ans = max(ans, f)
        
        return ans
