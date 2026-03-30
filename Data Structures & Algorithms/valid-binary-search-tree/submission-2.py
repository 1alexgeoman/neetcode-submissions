# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     ans = [root]
    #     counter = 0
    #     while counter<len(ans):
    #         node = ans[counter] 
    #         if node.left:
    #             ans.append(node.left)
    #             print (node.val,node.left.val)
    #             if node.val<=node.left.val:
    #                 return False
    #         if node.right:
    #             print (node.val,node.right.val)
    #             ans.append(node.right)
    #             if node.val>=node.right.val:
    #                 return False
    #         counter+=1
    #     return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
            
        # Store tuples: (node, lower_bound, upper_bound)
        queue = [(root, -float('inf'), float('inf'))]
        
        while queue:
            node, low, high = queue.pop(0)
            
            if not (low < node.val < high):
                return False
            
            if node.left:
                # Left child must be < node.val
                queue.append((node.left, low, node.val))
            if node.right:
                # Right child must be > node.val
                queue.append((node.right, node.val, high))
                
        return True
