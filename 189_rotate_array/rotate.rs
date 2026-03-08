impl Solution {
    pub fn rotate(nums: &mut Vec<i32>, k: i32) {
        let mut k = k as usize % nums.len();

        nums[..].reverse();
        nums[0..k].reverse();
        nums[k..].reverse();
    }
}
