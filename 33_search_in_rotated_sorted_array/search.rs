impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let n = nums.len();

        let mut l = 0;
        let mut r = n as i32 - 1;

        while l <= r {
            let m = l + (r - l) / 2;

            if nums[m as usize] == target {
                return m;
            }

            if  nums[l as usize] <= nums[m as usize] {
                if nums[m as usize] >= target && nums[l as usize] <= target {
                    r = m - 1;
                } else {
                    l = m + 1;
                }
            } else {
                if nums[m as usize] <= target && target <= nums[r as usize] {
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }
        }

        return -1;
    }
}