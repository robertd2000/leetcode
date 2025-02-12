/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseBetween(head *ListNode, left int, right int) *ListNode {
	dummy := &ListNode{
		Val:  0,
		Next: head,
	}

	prev := dummy

	for _ = range left - 1 {
		prev = prev.Next
	}

	curr := prev.Next

	for _ = range right - left {
		temp := curr.Next
		curr.Next = temp.Next
		temp.Next = prev.Next
		prev.Next = temp
	}

	return dummy.Next
}