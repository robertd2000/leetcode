/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	root := new(ListNode)
	carry := 0

	for n := root; l1 != nil || l2 != nil || carry > 0; n = n.Next {
		if l1 != nil {
			carry += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			carry += l2.Val
			l2 = l2.Next
		}
		val := carry % 10
		n.Next = &ListNode{val, nil}
		carry /= 10
	}

	return root.Next
}