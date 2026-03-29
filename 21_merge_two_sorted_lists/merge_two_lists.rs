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
    pub fn merge_two_lists(list1: Option<Box<ListNode>>, list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut l1 = list1;
        let mut l2 = list2;

        let mut dummy = Box::new(ListNode::new(0));
        let mut curr = &mut dummy;

        while l1.is_some() && l2.is_some() {
            if l1.as_ref().unwrap().val <= l2.as_ref().unwrap().val {
                let mut node = l1.take().unwrap();
                l1 = node.next.take();
                curr.next = Some(node);
            } else {
                let mut node = l2.take().unwrap();
                l2 = node.next.take();
                curr.next = Some(node);
            }

            curr = curr.next.as_mut().unwrap();
        }

        curr.next = if l1.is_some() { l1 } else { l2 };
        
        dummy.next
    }
}