use std::collections::HashSet;

impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack: Vec<i32> = Vec::new();
        let operations: HashSet<&str> = ["+", "-", "*", "/"].iter().cloned().collect();

        for t in &tokens {
            if operations.contains(t.as_str()) {
                let b = stack.pop().unwrap();
                let a = stack.pop().unwrap();
                let res = match t.as_str() {
                    "+" => a + b,
                    "-" => a - b,
                    "*" => a * b,
                    "/" => a / b,
                    _ => unreachable!(),
                };
                stack.push(res);
            } else {
                stack.push(t.parse::<i32>().unwrap());
            }
        }
        return stack.last().copied().unwrap();
    }

}