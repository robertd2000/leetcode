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
use std::cmp;

impl Solution {
    pub fn is_balanced(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        if let Some(node) = root {
            let right = node.borrow().right.clone();
            let left = node.borrow().left.clone();
            let left_val = Solution::get_height(left.clone());
            let right_val = Solution::get_height(right.clone());

            let skew = (left_val - right_val).abs();

            if skew > 1 {
                return false;
            }

            if !Solution::is_balanced(left) {
                return false;
            }

            if !Solution::is_balanced(right) {
                return false;
            }

            return true;
        } 

        return true;
    }

    pub fn get_height(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        if let Some(node) = root {
            let right = node.borrow().right.clone();
            let left = node.borrow().left.clone();
            let left_val = Solution::get_height(left);
            let right_val = Solution::get_height(right);

            return cmp::max(left_val, right_val) + 1;
        } else {
            return 0;
        }
    }
}