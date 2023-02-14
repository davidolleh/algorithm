from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if root is None:
            return []

        self._retList = []
        self.recurPathSum(node=root,targetSum=targetSum,crntList=[])

        return self._retList

    def recurPathSum(self, node:TreeNode, targetSum: int, crntList: List[int]):
        if node.left is None and node.right is None:
            if node.val == targetSum:
                crntList.append(node.val)
                self._retList.append(crntList.copy())
                crntList.pop()
            return


        newTargetSum = targetSum - node.val
        if node.left:
            crntList.append(node.val)
            self.recurPathSum(node=node.left,targetSum=newTargetSum,crntList=crntList)
            crntList.pop()
        if node.right:
            crntList.append(node.val)
            self.recurPathSum(node=node.right,targetSum=newTargetSum,crntList=crntList)
            crntList.pop()
        return



root = TreeNode(7)
node2n = TreeNode(-2)
node5 = TreeNode(5)
node3 = TreeNode(3)
node15 = TreeNode(15)
node8 = TreeNode(8)
node5n = TreeNode(-1)

root.left = node2n
root.right = node5
node2n.left = node3
node2n.right = node15
node5.left = node8
node5.right = node5n

s = Solution()
print(s.pathSum(root,20))