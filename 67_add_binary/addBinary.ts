function addBinary(a: string, b: string): string {
  const k = a.length;
  const m = b.length;

  const n = Math.max(k, m);

  a = a.split("").reverse().join("");
  b = b.split("").reverse().join("");

  let res = "";

  let carry = 0;

  for (let i = 0; i < n; i++) {
    const valA = i < k ? +a[i] : 0;
    const valB = i < m ? +b[i] : 0;

    const total = valA + valB + carry;
    const val = (total % 2).toString();
    res = val + res;
    carry = Math.floor(total / 2);
  }

  if (carry > 0) {
    res = "1" + res;
  }

  return res;
}
