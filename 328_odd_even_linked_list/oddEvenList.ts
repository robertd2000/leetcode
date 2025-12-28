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

function oddEvenList(head: ListNode | null): ListNode | null {
  if (head === null) return null;

  let odd = head;
  let even = head.next;
  let evenHead = even;

  while (even !== null && even.next !== null) {
    odd.next = odd.next!.next;
    even.next = even.next.next;

    odd = odd.next;
    even = even.next;
  }

  odd.next = evenHead;

  return head;
}
