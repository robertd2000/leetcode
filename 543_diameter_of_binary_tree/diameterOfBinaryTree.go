/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func diameterOfBinaryTree(root *TreeNode) int {
	diameter := 0

	var dfs func(root *TreeNode) int

	dfs = func(root *TreeNode) int {
		if root != nil {
			left := dfs(root.Left)
			right := dfs(root.Right)
			diameter = max(diameter, left+right)
			return max(left, right) + 1
		}

		return 0
	}

	dfs(root)

	return diameter
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}