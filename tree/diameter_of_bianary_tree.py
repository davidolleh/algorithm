class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root.left is None and root.right is None:
            return 0
        self.maxC = 0

        self.recursive(node=root)

        return self.maxC

    def recursive(self, node: TreeNode):
        l = 0
        r = 0
        if node.left is None and node.right is None:
            return 0

        if node.left:
            l = self.recursive(node=node.left)
            l = l + 1

        if node.right:
            r = self.recursive(node=node.right)
            r = r + 1

        if self.maxC < l + r:
            self.maxC = l + r

        return max(l, r)


root = TreeNode(val=1)
n1 = TreeNode(val=2)
n2 = TreeNode(val=4)
n3 = TreeNode(val=5)
n4 = TreeNode(val=3)
n5 = TreeNode(val=6)

root.left = n1
root.right = n4
n1.left=n2
n1.right= n3
n3.right=n5

s = Solution()
print(s.diameterOfBinaryTree(root=root))

