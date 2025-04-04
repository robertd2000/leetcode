#[derive(Default)]
struct MyQueue {
    input: Vec<i32>,
    output: Vec<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyQueue {

    fn new() -> Self {
        Default::default()
    }
    
    fn push(&mut self, x: i32) {
        self.input.push(x);
    }
    
    fn pop(&mut self) -> i32 {
        self.peek();
        self.output.pop().unwrap()
    }
    
    fn peek(&mut self) -> i32 {
        if self.output.is_empty() {
            while !self.input.is_empty() {
                self.output.push(self.input.pop().unwrap());
            }
        }

        return *self.output.last().unwrap();
    }
    
    fn empty(&self) -> bool {
        self.input.is_empty() && self.output.is_empty()
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * let obj = MyQueue::new();
 * obj.push(x);
 * let ret_2: i32 = obj.pop();
 * let ret_3: i32 = obj.peek();
 * let ret_4: bool = obj.empty();
 */