impl Solution {
    pub fn plus_one(mut digits: Vec<i32>) -> Vec<i32> {
        for x in digits.iter_mut().rev() {
            if *x + 1 < 10 {
                *x += 1;
                return digits;
            }

            *x =  0;
        }

        digits.insert(0, 1);
        digits
    }
}