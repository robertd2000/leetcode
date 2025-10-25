package sametree

//   Definition for a binary tree node.
type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}
 
func isSameTree(p *TreeNode, q *TreeNode) bool {
	type StackNode struct {
		n *TreeNode
		m *TreeNode
	}
	stack := []StackNode{
		{p, q},
	}

	for len(stack) > 0 {
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		if node.n == nil && node.m == nil {
			continue
		} else if node.n == nil || node.m == nil {
			return false
		} else {
			if node.n.Val != node.m.Val {
				return false
			}

			stack = append(stack, StackNode{node.n.Right, node.m.Right})
			stack = append(stack, StackNode{node.n.Left, node.m.Left})
		}

	}
	
	return true
}