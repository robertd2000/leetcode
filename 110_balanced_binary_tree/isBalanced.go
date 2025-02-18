/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isBalanced(root *TreeNode) bool {
	if root != nil {
		left := getHeight(root.Left)
		right := getHeight(root.Right)
		skew := abs(left, right)

		if !isBalanced(root.Left) {
			return false
		}
		if !isBalanced(root.Right) {
			return false
		}
		if skew > 1 {
			return false
		}

		return true
	}

	return true
}

func getHeight(root *TreeNode) int {
	if root != nil {
		left := getHeight(root.Left)
		right := getHeight(root.Right)

		return max(left, right) + 1
	}

	return 0
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}

func abs(a, b int) int {
	c := a - b
	if c < 0 {
		return -c
	}

	return c
}
