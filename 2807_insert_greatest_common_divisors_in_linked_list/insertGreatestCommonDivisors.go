package insertgreatestcommondivisorsinlinkedlist

// Definition for singly-linked list.

type ListNode struct {
	Val  int
	Next *ListNode
}

func insertGreatestCommonDivisors(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	prev := head
	curr := head.Next

	for curr != nil {
		val := gcd(prev.Val, curr.Val)
		node := &ListNode{Val: val, Next: curr}
		prev.Next = node
		prev = curr
		curr = curr.Next
	}

	return head
}

func gcd(a int, b int) int {
	for b != 0 {
		a, b = b, a%b
	}

	return a
}
