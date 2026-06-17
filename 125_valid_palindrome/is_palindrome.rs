impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let new_str: String = s.chars()
            .filter(|c| c.is_alphanumeric())
            .map(|c| c.to_ascii_lowercase())
            .collect();
        new_str == new_str.chars().rev().collect::<String>()
    }
}