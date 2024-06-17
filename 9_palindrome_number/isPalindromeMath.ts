function isPalindrome(x: number): boolean {
  if (x < 0) return false;

  let reversed_num = 0;
  let temp = x;

  while (temp != 0) {
    let digit = temp % 10;
    reversed_num = reversed_num * 10 + digit;
    temp = Math.floor(temp / 10);
  }

  return reversed_num === x;
}
