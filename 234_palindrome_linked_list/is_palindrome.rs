// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn is_palindrome(mut head: Option<Box<ListNode>>) -> bool {
        let mut len = 0;
        let mut cur = &head;
        while let Some(node) = cur {
            cur = &node.next;
            len += 1;
        }

        let mut cur = &mut head;
        for _ in 0..(len - 1) / 2 {
            cur = &mut cur.as_mut().unwrap().next;
        }

        let mut prev = None;
        let mut cur = cur.as_mut().unwrap().next.take();
        while let Some(mut node) = cur {
            cur = node.next;
            node.next = prev;
            prev = Some(node);
        }

        let mut right_part = &prev;
        let mut left_part = &head;
        while let (Some(r), Some(l)) = (right_part, left_part) {
            if r.val != l.val {
                return false;
            }
            right_part = &r.next;
            left_part = &l.next;
        }
        true
    }
}