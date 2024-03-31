impl TwoSum {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let mut l = 0;
        let mut r = numbers.len() - 1;

        while l < r {
            if numbers[l] + numbers[r] == target {
                return vec![(l + 1) as i32, (r + 1) as i32];
            }

            if numbers[l] + numbers[r] > target {
                 r = r - 1;
            }

            if numbers[l] + numbers[r] < target {
                 l = l + 1;
            }
        }

         vec![0, 0]
    }
}