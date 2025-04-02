impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut count = 1;
        let mut major = nums[0];

        for i in 1..nums.len() {
            if count <= 0 {
                count = 1;
                major = nums[i];
            } else if nums[i] == major {
                count += 1;
            } else {
                count -= 1;
            }
        }
        return major;
    }
}
