
class Solution:
    def resultArray(self, nums, k):
        result = [0] * k
        
        # dp[r] = number of subarrays ending at previous index
        # whose product % k == r
        dp = [0] * k
        
        for num in nums:
            new_dp = [0] * k
            
            # Start a new subarray with nums[i]
            r = num % k
            new_dp[r] += 1
            
            # Extend all previous subarrays
            for rem in range(k):
                if dp[rem]:
                    new_rem = (rem * num) % k
                    new_dp[new_rem] += dp[rem]
            
            # Add subarrays ending here to answer
            for rem in range(k):
                result[rem] += new_dp[rem]
            
            dp = new_dp
        
        return result
