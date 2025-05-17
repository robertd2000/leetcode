/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func kthSmallest(root *TreeNode, k int) int {
    var stack []*TreeNode

    for root != nil {
        stack = append(stack, root)
        root = root.Left
    }

    for k != 0 {
        n := stack[len(stack)-1]
        stack = stack[:len(stack)-1]

        k -= 1

        if k == 0 {
            return n.Val
        }

        r := n.Right

        for r != nil {
            stack = append(stack, r)
            r = r.Left
        }
    }

    return -1
}