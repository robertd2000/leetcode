[232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/description/)

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).

Implement the `MyQueue` class:

- `void push(int x)` Pushes element x to the back of the queue.
- `int pop()` Removes the element from the front of the queue and returns it.
- `int peek()` Returns the element at the front of the queue.
- `boolean empty()` Returns `true` if the queue is empty, `false` otherwise.

**Notes:**

- You must use **only** standard operations of a stack, which means only `push to top`, `peek/pop from top`, `size`, and `is empty` operations are valid.
- Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

**Example 1:**

**Input**
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
**Output**
[null, null, null, 1, 1, false]

**Explanation**
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false

**Constraints:**

- `1 <= x <= 9`
- At most `100` calls will be made to `push`, `pop`, `peek`, and `empty`.
- All the calls to `pop` and `peek` are valid.

**Follow-up:** Can you implement the queue such that each operation is **[amortized](https://en.wikipedia.org/wiki/Amortized_analysis)** `O(1)` time complexity? In other words, performing `n` operations will take overall `O(n)` time even if one of those operations may take longer.

```typescript
class MyQueue {
  input: number[];
  output: number[];

  constructor() {
    this.input = [];
    this.output = [];
  }

  push(x: number): void {
    this.input.push(x);
  }

  pop(): number {
    this.peek();
    return this.output.pop();
  }

  peek(): number {
    if (this.output.length === 0) {
      while (this.input.length) {
        this.output.push(this.input.pop());
      }
    }

    return this.output[this.output.length - 1];
  }

  empty(): boolean {
    return this.output.length === 0 && this.input.length === 0;
  }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */
```

```python

class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return not self.output and not self.input


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


```

```cpp

class MyQueue {
public:
    stack<int> input;
    stack<int> output;

    MyQueue() {}

    void push(int x) { input.push(x); }

    int pop() {
        int val = peek();
        output.pop();
        return val;
    }

    int peek() {
        if (output.empty()) {
            while (!input.empty()) {
                int val = input.top();
                input.pop();
                output.push(val);
            }
        }

        return output.top();
    }

    bool empty() { return input.empty() && output.empty(); }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */

```

```java

class MyQueue {
    private Stack<Integer> input = new Stack<>();
    private Stack<Integer> output = new Stack<>();

    public MyQueue() {

    }

    public void push(int x) {
        input.push(x);
    }

    public int pop() {
        peek();
        return output.pop();
    }

    public int peek() {
        if (output.empty()) {
            while (!input.empty()) {
                int val = input.pop();
                output.push(val);
            }
        }

        return output.peek();
    }

    public boolean empty() {
        return input.empty() && output.empty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */

```

```go

type MyQueue struct {
    input []int
    output []int
}


func Constructor() MyQueue {
    return MyQueue{}
}


func (this *MyQueue) Push(x int)  {
    this.input = append(this.input, x)
}


func (this *MyQueue) Pop() int {
    val := this.Peek()
    this.output = this.output[:len(this.output) - 1]
    return val
}


func (this *MyQueue) Peek() int {
    if len(this.output) == 0 {
        for len(this.input) > 0 {
            this.output = append(this.output, this.input[len(this.input) - 1])
            this.input = this.input[:len(this.input) - 1]
        }
    }
    return this.output[len(this.output) - 1]
}


func (this *MyQueue) Empty() bool {
    return len(this.input) == 0 && len(this.output) == 0
}


/**
 * Your MyQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Peek();
 * param_4 := obj.Empty();
 */

```
