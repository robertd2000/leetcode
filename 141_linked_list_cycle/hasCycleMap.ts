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

function hasCycle(head: ListNode | null): boolean {
  const visited = new Map();

  while (head && head.next) {
    if (visited.has(head)) {
      return true;
    } else {
      visited.set(head, true);
    }
    head = head.next;
  }

  return false;
}
