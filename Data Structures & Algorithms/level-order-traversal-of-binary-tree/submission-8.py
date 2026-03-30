# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # ans = [root]
        # print(ans)
        # if ans == [None]:
        #     return []
        # anns = []
        # counter = 0
        # explored = True
        # while explored == True:
        #     if not ans[counter].left and not ans[counter].right and counter == len(ans)-1:
        #         explored = False
        #     if ans[counter].left:
        #         ans.append(ans[counter].left)
            
        #     if ans[counter].right:
        #         ans.append(ans[counter].right)
        #     counter +=1
        # print(ans)
        # for i in range(0,int(math.log(len(ans),2))+1):
        #     print("i",i,"ii",2**i)
        #     array = [ans[x].val for x in range(2**i-1,(2**(i+1)-1)) if x<len(ans)]
        #     anns.append(array)
        
        # print(anns)
        # return (anns)

        if not root:
            return []
        ans = [(root,0)]
        counter = 0

        while counter < len(ans):
            node, level = ans[counter]

            if node.left:
                ans.append((node.left, level+1))
            if node.right:
                ans.append((node.right, level+1))
            counter+=1

        finalAns = []
        for item in ans:
            node, level = item
            if len(finalAns)<=level:
                finalAns.append([])
            finalAns[level].append(node.val)
        return(finalAns)


         
        