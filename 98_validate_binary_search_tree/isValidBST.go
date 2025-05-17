/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isValidBST(root *TreeNode) bool {
	return dfs(root, math.MinInt, math.MaxInt)
}

func dfs(root *TreeNode, minVal int, maxVal int) bool {
	if root == nil {
		return true
	}

	if root.Val <= minVal || root.Val >= maxVal {
		return false
	}

	return dfs(root.Left, minVal, root.Val) && dfs(root.Right, root.Val, maxVal)
}