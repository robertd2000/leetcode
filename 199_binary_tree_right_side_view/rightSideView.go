/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func rightSideView(root *TreeNode) []int {
    res := make([]int, 0)

    dfs(root, 0, &res)

    return res
}

func dfs(root *TreeNode, level int, res *[]int) {
    if root != nil {
        if len(*res) <= level {
            *res = append(*res, root.Val)
        }

        (*res)[level] = root.Val

        dfs(root.Left, level + 1, res)
        dfs(root.Right, level + 1, res)
    }
}