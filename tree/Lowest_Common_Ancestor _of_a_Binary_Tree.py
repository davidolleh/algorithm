class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None and root is None:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        l = self.lowestCommonAncestor(root=root.left, p=p,q=q)
        r = self.lowestCommonAncestor(root=root.right, p=p,q=q)

        if l and r:
            return root

        return r if l is None else l
        # self.pParent = []
        # self.qParent = []
        # self.parent = []
        #
        # self.recursive(node=root,p=p,q=q)
        # result = root
        #
        # for i in self.pParent:
        #     for j in self.qParent:
        #         if i.val == j.val:
        #             result = i
        #
        # return result

    def recursive(self, node: TreeNode, p: TreeNode, q: TreeNode):
        self.parent.append(node)

        if p.val == node.val:
            self.pParent = self.parent.copy()

        if q.val == node.val:
            self.qParent = self.parent.copy()

        if node.left is None and node.right is None:
            return

        if node.left:
            self.recursive(node=node.left,p=p,q=q)
            self.parent.pop()

        if node.right:
            self.recursive(node=node.right,p=p,q=q)
            self.parent.pop()

root = TreeNode(x=3)
p = TreeNode(x=5)
q = TreeNode(x=1)
a6 = TreeNode(x=6)
a2 = TreeNode(x=2)
a7 = TreeNode(x=7)
a4 = TreeNode(x=4)
a0 = TreeNode(x=0)
a8 = TreeNode(x=8)

root.left = p
root.right = q
p.left = a6
p.right=a2
a2.left=a7
a2.right=a4
q.left=a0
q.right= a8

s = Solution()
print(s.lowestCommonAncestor(root=root, p=p, q=a4).val)