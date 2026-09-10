class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        ans = 0
        
        def dfs(node):
            nonlocal ans
            
            if node is None:
                return 0, 0   # sum, count
            
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            total_sum = node.val + left_sum + right_sum
            total_count = 1 + left_count + right_count
            
            average = total_sum // total_count
            
            if node.val == average:
                ans += 1
            
            return total_sum, total_count
        
        dfs(root)
        return ans
