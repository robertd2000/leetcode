package intersectionoftwolinkedlists

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func getIntersectionNode(headA, headB *ListNode) *ListNode {
	p1, p2 := headA, headB

	if p1 == nil || p2 == nil {
		return nil
	}

	for p1 != nil && p2 != nil && p1 != p2 {
		p1 = p1.Next
		p2 = p2.Next

		if p1 == p2 {
			return p1
		}

		if p1 == nil {
			p1 = headB
		}

		if p2 == nil {
			p2 = headA
		}
	}

	return p1
}
