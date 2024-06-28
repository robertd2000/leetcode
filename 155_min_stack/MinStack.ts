class MinStack {
  stack: number[];
  minStack: number[];
  currentMin: number;

  constructor() {
    this.stack = [];
    this.minStack = [];
    this.currentMin = Infinity;
  }

  push(val: number): void {
    this.stack.push(val);

    if (val <= this.currentMin) {
      this.minStack.push(this.currentMin);
      this.currentMin = val;
    }
  }

  pop(): void {
    const value = this.stack.pop();

    if (value === this.currentMin) {
      this.currentMin = this.minStack[this.minStack.length - 1];
      this.minStack.pop();
    }
  }

  top(): number {
    return this.stack[this.stack.length - 1];
  }

  getMin(): number {
    return this.currentMin;
  }
}
