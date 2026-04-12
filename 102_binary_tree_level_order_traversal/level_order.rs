// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;
impl Solution {
    pub fn level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        if let Some(root_node) = root {
            let mut q = VecDeque::from(vec![root_node.clone()]);
            let mut ans = vec![vec![root_node.borrow().val]];

            while !q.is_empty() {
                let total_nodes_in_level = q.len();
                let mut level_nodes = vec![];
                for _ in 0..total_nodes_in_level {
                    let node = q.pop_front().unwrap();
                    if let Some(left) = node.borrow().left.clone() {
                        q.push_back(left.clone());
                        level_nodes.push(left.borrow().val);
                    }
                    if let Some(right) = node.borrow().right.clone() {
                        q.push_back(right.clone());
                        level_nodes.push(right.borrow().val);
                    }
                }

                if !level_nodes.is_empty() {
                    ans.push(level_nodes);
                }
            }

            ans
        } else {
            vec![]
        }
    }
}