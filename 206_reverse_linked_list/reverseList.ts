function reverseList(head: ListNode | null): ListNode | null {
  let curr = head;
  let prev = null;

  while (curr != null) {
    let next = curr.next;
    curr.next = prev;
    prev = curr;
    curr = next;
  }

  return prev;
}
