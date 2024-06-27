class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return
            
        res = [[root.val]]
        
        q = [root]
        t = []

        while len(q) > 0:
            cur = q.pop(0)

            if cur.left is not None:
                t.append(cur.left)
            if cur.right is not None:
                t.append(cur.right)
            if not q:
                if t:
                    res.append([n.val for n in t])
                q = t
                t = []

        return res