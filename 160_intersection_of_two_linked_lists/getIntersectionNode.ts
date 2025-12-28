/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function getIntersectionNode(
  headA: ListNode | null,
  headB: ListNode | null
): ListNode | null {
  let p1 = headA;
  let p2 = headB;

  if (p1 === null || p2 === null) return null;

  while (p1 !== null && p2 !== null && p1 !== p2) {
    p1 = p1.next;
    p2 = p2.next;

    if (p1 === p2) return p1;

    if (p1 === null) p1 = headB;
    if (p2 === null) p2 = headA;
  }

  return p1;
}
