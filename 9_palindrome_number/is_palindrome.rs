impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 {
            return false;
        }

        let mut temp = x;
        let mut rev = 0;

        while temp != 0 {
            let digit = temp % 10;
            rev = rev * 10 + digit;
            temp = temp / 10;
        }

        rev == x
    }
}