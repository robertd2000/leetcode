//Definition for singly-linked list.
class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function insertGreatestCommonDivisors(head: ListNode | null): ListNode | null {
  if (head == null) return head;

  let prev = head;
  let curr = head.next;

  while (curr != null) {
    let val = gcd(prev.val, curr.val);
    let node = new ListNode(val, curr);
    prev.next = node;
    prev = curr;
    curr = curr.next;
  }

  return head;
}

function gcd(a: number, b: number): number {
  while (b != 0) {
    let temp = a;
    a = b;
    b = temp % b;
  }
  return a;
}
