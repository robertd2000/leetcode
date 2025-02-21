/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func maxDepth(root *TreeNode) int {
	depth := 0

	var dfs func(root *TreeNode) int

	dfs = func(root *TreeNode) int {
		if root != nil {
			left := dfs(root.Left)
			right := dfs(root.Right)
			d := max(left, right) + 1
			depth = max(depth, d)
			return d
		}

		return 0
	}

	dfs(root)

	return depth
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}
